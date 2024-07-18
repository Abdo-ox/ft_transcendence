from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-_^@m%$xt&8mynfeu4w7c!i4@w7)2f(jegj%vey9v+_-w^yz9px'
DEBUG = True

ALLOWED_HOSTS = []

AUTH_USER_MODEL = 'user.User'

AUTHENTICATION_BACKENDS = [
    'user.auth.MyBackend',  
    'django.contrib.auth.backends.ModelBackend',
]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'user',
    'project'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'project.urls'

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

WSGI_APPLICATION = 'project.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'test',
        'USER': 'postgres',
        'PASSWORD': 'hello',
        'HOST': 'localhost',
        'port': '5432',
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

OAUTH_CONFIG = {
    '42': {
        'client_id': 'u-s4t2ud-589237e6394550420d14a9a59740b48214effbb5b50d9943c952f85a1e639e46',
        'client_secret': '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',
        'redirect_uri': 'http://localhost:8000/auth/42/callback',
        'base_url': 'https://api.intra.42.fr/oauth/authorize',
        'token_url': 'https://api.intra.42.fr/oauth/token',
        'info_url': ' https://api.intra.42.fr/v2/me',
    }
}

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

STATIC_URL = 'static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
