# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases
import os

BASE_DIR = os.path.dirname(os.path.dirname(file))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
