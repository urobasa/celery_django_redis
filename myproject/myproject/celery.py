import os
from celery import Celery

# Указываем Django, где находятся настройки
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

# Создаем экземпляр Celery
app = Celery('myproject')

# Загружаем настройки из Django
app.config_from_object('django.conf:settings', namespace='CELERY')

# Автоматически находим и регистрируем задачи в приложениях Django
app.autodiscover_tasks()

