from django.utils.translation import gettext_lazy as _

from .django_settings import *

INSTALLED_APPS += (
    # 'corsheaders',
    'wooey',
)

MIDDLEWARE = list(MIDDLEWARE)
MIDDLEWARE_OBJ = MIDDLEWARE

LANGUAGES = [
  ('de', _('German')),
  ('en', _('English')),
  ('fr', _('French')),
  ('ja', _('Japanese')),
  ('nl', _('Dutch')),
  ('zh-hans', _('Simplified Chinese')),
]

NEW_MIDDLEWARE = []
for i in MIDDLEWARE_OBJ:
    NEW_MIDDLEWARE.append(i)
    if i == 'django.contrib.sessions.middleware.SessionMiddleware':
        NEW_MIDDLEWARE.append('django.middleware.locale.LocaleMiddleware')

NEW_MIDDLEWARE.append('cuddlymachine.middleware.ProcessExceptionMiddleware')
MIDDLEWARE = NEW_MIDDLEWARE

PROJECT_NAME = "cuddlymachine"
WOOEY_CELERY_APP_NAME = 'wooey.celery'
WOOEY_CELERY_TASKS = 'wooey.tasks'
WOOEY_SITE_NAME = "Biohacker"
WOOEY_SITE_TAG = "A python scripts for biology"