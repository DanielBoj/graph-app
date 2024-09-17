FROM python:3.12

WORKDIR /app

ADD ./ /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD ["gunicorn", "main:app"]