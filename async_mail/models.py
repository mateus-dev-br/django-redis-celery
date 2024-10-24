from django.db import models
from django.contrib.auth.models import User

class EmailTask(models.Model):
    emails = models.TextField()
    subject = models.CharField(max_length=50) 
    message = models.TextField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    is_sent = models.BooleanField(default=False)

    def __str__(self):
        return f'Task for {self.emails} - Sent: {self.is_sent}'

    def get_email_list(self):
        return [email.strip() for email in self.emails.split(',')]