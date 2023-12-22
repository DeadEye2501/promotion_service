import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'promotion_service.settings')

app = Celery('promotion_service')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'check_polygon_api': {
        'task': 'core.tasks.check_polygon_api',
        'schedule': crontab(hour='0', minute='0'),
    },
}
