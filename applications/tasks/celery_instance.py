import os

import django
from celery import Celery, platforms
from config.settings import CELERY_DEV_ENV

from applications.tasks import celery_config

platforms.C_FORCE_ROOT = True

RABBIT_MQ_USER = "root"
RABBIT_MQ_PASSWORD = "root"
RABBIT_MQ_PORT = 5672
if CELERY_DEV_ENV:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.dev')
    RABBIT_MQ_IP = "127.0.0.1"
else:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.prod')
    RABBIT_MQ_IP = "rabbitmq"

django.setup()

app = Celery(
    "celery",
    broker="amqp://{0}:{1}@{2}:{3}/broker".format(
        RABBIT_MQ_USER, RABBIT_MQ_PASSWORD, RABBIT_MQ_IP, RABBIT_MQ_PORT
    )
)

app.config_from_object(celery_config, silent=True, force=True)

# celery worker -A async_task.celery_instance -l info --pool=solo   error
# celery -A applications.tasks.celery_instance worker -l info --pool=solo 正确启动
# celery -A applications.tasks.celery_instance beat -l info  定时任务
