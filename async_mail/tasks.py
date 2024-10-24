# tasks.py
from celery import shared_task
from django.core.mail import send_mail
from .models import EmailTask
from decouple import config

@shared_task
def send_email_task(email_task_id):
    email_task = EmailTask.objects.get(id=email_task_id)
    send_mail(
        email_task.subject,
        email_task.message,
        config('EMAIL_HOST_USER'),
        email_task.get_email_list(),
        fail_silently=False,
    )
    email_task.is_sent = True
    email_task.save()