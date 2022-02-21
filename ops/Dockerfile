FROM python:3.8-buster

ENV PYTHONUNBUFFERED=1

WORKDIR /usr/src/app
COPY requirements.txt ./
RUN  rm -Rf /var/lib/apt/lists/* && apt-get update && \
     pip3 install --no-cache-dir -r requirements.txt
COPY . .
CMD python3 manage.py migrate --settings config.prod && \
    uwsgi -d --ini uwsgi.ini && \
    nohup & celery -A applications.tasks.celery_instance worker -l info && \
    nohup & celery -A applications.tasks.celery_instance beat -l info
