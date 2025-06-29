import os
from celery import Celery

# Set default Django settings module for the 'celery' command-line program
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

# Initialize Celery application
app = Celery('config')

# Load Celery settings from Django settings using the 'CELERY_' namespace
app.config_from_object('django.conf:settings', namespace='CELERY')

# Auto-discover task modules in all Django apps
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    """
    A simple debug task to test Celery worker setup.
    Usage: debug_task.delay()
    """
    print(f"[DEBUG] Request: {self.request!r}")

