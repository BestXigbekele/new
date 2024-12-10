"""
WSGI config for pro_list project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

from django.core.management import call_command
from django.contrib.auth import get_user_model

User = get_user_model()

def create_superuser():
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser('admin', 'admin@example.com', 'password')  # Change as needed

if os.environ.get('RUN_MAIN') == 'true':  # Only run in development mode
    create_superuser()
  
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pro_list.settings')

application = get_wsgi_application()
