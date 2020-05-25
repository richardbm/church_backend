import os

from celery import Celery

# Set default Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'church_project.settings')

app = Celery('church_project')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
