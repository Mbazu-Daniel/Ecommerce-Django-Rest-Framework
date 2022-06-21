import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "storefront.settings.dev")

celery = Celery("storefront")

# set where celery can find configuration variables
celery.config_from_object("django.conf:settings", namespace="CELERY")
celery.autodiscover_tasks()
