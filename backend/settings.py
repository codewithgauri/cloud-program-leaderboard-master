import os
from decouple import config
import django_heroku

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = config('SECRET_KEY')

DEBUG = False

ALLOWED_HOSTS = []


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'core',
    'rest_framework',
    'django_celery_beat', 
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'backend.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'backend.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]



LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'

CELERY_BROKER_URL = config('REDIS_URL')
CELERY_RESULT_BACKEND = config('REDIS_URL')
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TASK_SERIALIZER = 'json'

USERS_URLS = [
    "https://www.qwiklabs.com/public_profiles/8dc90af5-ba5e-45de-b73b-6f19bda4a40b",
"https://www.qwiklabs.com/public_profiles/7c66e0fa-353f-400b-be1e-9ebd0755de79",
"https://www.qwiklabs.com/public_profiles/e347992a-adde-4c3a-b18d-f5506200e71d",
"https://www.qwiklabs.com/public_profiles/34b07043-4a83-4fba-8da1-a93a8a9d2625",
"https://www.qwiklabs.com/public_profiles/28ce8631-1a30-4b45-b9b8-c1739debe91b",
"https://www.qwiklabs.com/public_profiles/4e1a445f-7ace-4a3e-bf13-f4a1b5b2dc28",
"https://google.qwiklabs.com/public_profiles/f78b2940-37df-428d-978a-93903357e0d3",
"https://www.qwiklabs.com/public_profiles/cd8a2727-d0e6-4f1d-b75a-a8c120162412",
"https://google.qwiklabs.com/public_profiles/d0ac8b3b-5ec5-4fda-a197-81cab8de4526",
"https://www.qwiklabs.com/public_profiles/56c788a5-a3fa-4c77-890c-c994205920ac",
"https://www.qwiklabs.com/public_profiles/50e77248-d661-41f9-90f4-c5584fb3b7db",
"https://google.qwiklabs.com/public_profiles/30156fc2-0477-4fdc-bff9-2f2827e6d959",
"https://google.qwiklabs.com/public_profiles/83fe28cd-685a-4481-968f-efefc16b0393",
"https://www.qwiklabs.com/public_profiles/ff55cb71-b10b-4d10-a2bc-8190cb2ed4d2",
"https://www.qwiklabs.com/public_profiles/af2d8aa5-8794-4cc9-8942-9597c2c5355e",
"https://www.qwiklabs.com/public_profiles/84a9eb53-fa55-46d4-a774-f8ba0f393373",
"https://www.qwiklabs.com/public_profiles/ea1b493e-7967-4c41-9541-c562eebbc627",
"https://google.qwiklabs.com/public_profiles/b079e238-df06-439f-b0c5-f5e3388e2942",
"https://www.qwiklabs.com/public_profiles/d653e308-9741-41a3-a41f-322985893c48",
"https://google.qwiklabs.com/public_profiles/f7c09c86-2eab-4d97-9ce1-bb5aa7907980",
"https://google.qwiklabs.com/public_profiles/bbe89358-5647-4765-9500-847faf7b0e59",
"https://google.qwiklabs.com/public_profiles/0e2b73b7-e9ce-4208-abd6-d9d40f41286b",
"https://www.qwiklabs.com/public_profiles/f4354ab9-6c6a-4b48-8063-107fa187f8ea",
"https://www.qwiklabs.com/public_profiles/6a26d090-2807-41a6-a1b1-9aa5e3a0d2f5",
"https://www.qwiklabs.com/public_profiles/cb88bda4-fd34-4360-b7dd-060cc2de02f3",
"https://www.qwiklabs.com/public_profiles/cb88bda4-fd34-4360-b7dd-060cc2de02f3",
"https://www.qwiklabs.com/public_profiles/355113ef-9104-494c-9bb6-a105c0cb5ebb",
"https://www.qwiklabs.com/public_profiles/7e2babfc-b251-4e44-9c06-3608516b8082",
"https://www.qwiklabs.com/public_profiles/45ad99e07-b220-7d92ffca05147a-740f-4",
"https://google-run.qwiklabs.com/public_profiles/ee919f07-df02-4fb7-9060-3bd2f9d9957e",
"https://www.qwiklabs.com/public_profiles/ee919f07-df02-4fb7-9060-3bd2f9d9957e",
"https://google.qwiklabs.com/public_profiles/95a1d3a2-08f0-4d0c-8e39-8021648f9181",
"https://www.qwiklabs.com/public_profiles/abded8ac-dfb8-4406-9c15-7b22e9e7cf46",
"https://google.qwiklabs.com/public_profiles/7270e916-24e1-43bf-a255-c381076320e6",
"https://www.qwiklabs.com/public_profiles/11c31b39-3867-4590-820d-9b36654759c2",
"https://google.qwiklabs.com/public_profiles/48a16a00-a444-4413-820e-53f575b7ac66",

    ]


CORS_ORIGIN_ALLOW_ALL = True

CORS_ALLOW_HEADERS = [
    'accept',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
    'Cache-Control',
    'X-Requested-With',
]


CELERY_BEAT_SCHEDULE = {
    'generate-report': {
       'task': 'core.tasks.summary',
       'schedule': 30.0,
    },
     
}

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
    )
}


django_heroku.settings(locals())