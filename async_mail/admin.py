from django.contrib import admin

from .models import EmailTask

@admin.register(EmailTask)
class EmailTaskAdmin(admin.ModelAdmin):
    list_display = ('emails', 'subject', 'created_at', 'is_sent')
    search_fields = ('emails', 'subject')
    list_filter = ('is_sent',)