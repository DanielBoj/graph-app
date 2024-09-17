from app import create_app

app = create_app()

if __name__ == '__main__':

    # from gunicorn.app.wsgiapp import WSGIApplication as gunicorn
    # app = gunicorn(app)
    app.run(host= '0.0.0.0', port='5000')