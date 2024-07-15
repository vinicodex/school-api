# src/students/signals.py

import certifi
import ssl
import smtplib
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Student

def send_custom_email(subject, message, from_email, recipient_list):
    ssl_context = ssl.create_default_context(cafile=certifi.where())
    with smtplib.SMTP(settings.EMAIL_HOST, settings.EMAIL_PORT) as server:
        server.ehlo()
        if settings.EMAIL_USE_TLS:
            server.starttls(context=ssl_context)
            server.ehlo()
        server.login(settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASSWORD)
        server.sendmail(from_email, recipient_list, message)

@receiver(post_save, sender=Student)
def send_inactive_email(sender, instance, **kwargs):
    if not instance.is_active:
        subject = 'Student Marked as Inactive'
        message = f'The student {instance.name} has been marked as inactive.'
        from_email = settings.DEFAULT_FROM_EMAIL
        recipient_list = ['vinicodex@gmail.com']

        email_message = f"Subject: {subject}\n\n{message}"

        send_custom_email(subject, email_message, from_email, recipient_list)
