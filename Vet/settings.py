from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent


# =========================
# SECURITY
# =========================
SECRET_KEY = 'django-insecure-_myn$*#%=gu2@kig_92+aemkt+ktvpajc4!%t^hhwz)4paso$)'
DEBUG = False
ALLOWED_HOSTS = ['*']


# =========================
# APPLICATIONS
# =========================
INSTALLED_APPS = [
    'cloudinary',
    'cloudinary_storage',

    'app_vet',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]


# =========================
# MIDDLEWARE
# =========================
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',

    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


ROOT_URLCONF = 'Vet.urls'
WSGI_APPLICATION = 'Vet.wsgi.application'


# =========================
# TEMPLATES
# =========================
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


# =========================
# DATABASE
# =========================
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# =========================
# INTERNATIONALIZATION
# =========================
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True


# =========================
# STATIC FILES (WhiteNoise)
# =========================
STATIC_URL = 'static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]

STATIC_ROOT = os.path.join(BASE_DIR, 'static')

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
# =========================
# CLOUDINARY (MEDIA FILES)
# =========================
import cloudinary

CLOUDINARY_STORAGE = {
    'CLOUD_NAME': 'Root',
    'API_KEY': '169419662824352',
    'API_SECRET': 'ZSEX2',
}

DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'


 


# =========================
# DEFAULT AUTO FIELD
# =========================
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'