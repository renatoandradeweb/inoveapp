# app/inove/settings.py

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'inove',
    'rest_framework',
    'django_extensions',
]

# Configurações do banco de dados para o Django ORM
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'inoveapp',
        'USER': 'inove',
        'PASSWORD': 'inoveSucesso2024',
        'HOST': 'db',
        'PORT': '5432',
    }
}

# Configurações para o SQLAlchemy
SQLALCHEMY_DATABASE_URL = f"postgresql://{DATABASES['default']['USER']}:{DATABASES['default']['PASSWORD']}@{DATABASES['default']['HOST']}:{DATABASES['default']['PORT']}/{DATABASES['default']['NAME']}"

# Adicione sua SECRET_KEY
SECRET_KEY = 'LKK94HrBJ2wGyBl8IzRDsWvCYcGRJ4XlZi8zkSSqYUAjL9v9u2ucpD0_2QAAw_LCj60'

# Outras configurações comuns
ALLOWED_HOSTS = ['*']
DEBUG = True

# Configuração do middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Configuração das URLs e WSGI
ROOT_URLCONF = 'inove.urls'
WSGI_APPLICATION = 'inove.wsgi.application'

# Configuração para arquivos estáticos
STATIC_URL = '/static/'

# Configuração para arquivos de templates
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

# Configuração do idioma e fuso horário
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True
