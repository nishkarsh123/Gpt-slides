import os

from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "gpt_slides.settings")
app = Celery("gpt_slides")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()
