"""
WSGI config for sample_project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os
import sys
import codecs
from django.core.wsgi import get_wsgi_application

sys.stdout = codecs.getwriter("utf-8")(sys.stdout)
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/..')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sample_project.settings')

application = get_wsgi_application()
