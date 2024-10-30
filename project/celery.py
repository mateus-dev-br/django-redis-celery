from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# Define o módulo padrão do Django para o Celery.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

app = Celery('project')

# Carrega as configurações do Django.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Carrega as tarefas do Django.
app.autodiscover_tasks()

app.conf.broker_url = os.getenv('CELERY_BROKER_URL', 'redis://localhost:6379/0')