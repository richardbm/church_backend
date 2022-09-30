import os


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'church',
        'USER': 'root',
        'PASSWORD': 'development',
        'HOST': 'postgres',
        'PORT': '5432',
    },
}


STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
