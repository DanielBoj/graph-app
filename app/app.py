from flask import Flask, render_template
from flasgger import Swagger

from domain.stats_graphics import api_blueprint
from domain.app_version_handler import app_version_api_blueprint
import markdown as md

def create_app():

    app = Flask(__name__, template_folder = './presentation/templates', static_folder = './static')
    app.register_blueprint(api_blueprint)
    app.register_blueprint(app_version_api_blueprint)

    swagger = Swagger(app, template_file='swagger.yml')

    @app.route('/')
    def index():
        
        with open('./README.md', 'r') as mdf:
            markdown_content = mdf.read()
        
        html_content = md.markdown(markdown_content)

        return render_template('index.html', content=html_content)
    
    return app

if __name__ == '__main__':

    app = create_app()