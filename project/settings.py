# from project.settings.env import ABS_PATH, ENV_BOOL, ENV_STR, ENV_LIST, ENV_DEC, ENV_INT, BASE_DIR
import os

# import dj_database_url
from corsheaders.defaults import default_headers


from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

DEBUG = True
# DEBUG = ENV_BOOL("DEBUG", True)
# SECRET_KEY = ENV_STR("SECRET_KEY", "secret" if DEBUG else "")
SECRET_KEY = '^*%-h@4k__-glx0px%i#iym(1d^x54k6@--0mmlmc(-)w3+3_+'

# ALLOWED_HOSTS = ENV_LIST("ALLOWED_HOSTS", ",", ["*"] if DEBUG else [])
ALLOWED_HOSTS= ["*"]

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",

    "corsheaders",
    "rest_framework",
    "rest_framework.authtoken",
    "allauth",
    "allauth.account",
    "rest_auth",
    "rest_auth.registration",

    "customusers.apps.CustomUsersConfig",
    "core.apps.CoreConfig",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "project.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        # "DIRS": ['templates'],
        'DIRS': [BASE_DIR / 'templates'],
        # "DIRS": [ ENV_STR("BASE_DIR") / 'templates'],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ]
        },
    }
]

WSGI_APPLICATION = "project.wsgi.application"

# DATABASES = {"default": dj_database_url.config()}
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

AUTH_USER_MODEL = 'customusers.CustomUser'

AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

AUTHENTICATION_BACKENDS = (
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
)

# allauth settings

ACCOUNT_USER_MODEL_USERNAME_FIELD = None
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_EMAIL_REQUIRED = True

ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_EMAIL_VERIFICATION = "none"
LOGOUT_ON_PASSWORD_CHANGE = False
LOGIN_REDIRECT_URL = "/"



LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_L10N = True
USE_TZ = True

SITE_ID = 1

# static and media
# if STATIC_ROOT ends with STATIC_URL, it makes nginx static serve config easy, likewise for media
STATIC_URL = "/static/"
STATIC_ROOT =  "static"
MEDIA_URL =  "/media/"
MEDIA_ROOT =  "media"

# email settings
EMAIL_BACKEND = "django.core.mail.backends.{}.EmailBackend".format(
     "console"
)
EMAIL_HOST = "localhost"
EMAIL_HOST_USER = ""
EMAIL_HOST_PASSWORD =  ""
EMAIL_PORT =  25
EMAIL_USE_TLS =  False
SERVER_EMAIL =  "webmaster@localhost"
DEFAULT_FROM_EMAIL =  SERVER_EMAIL

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework.authentication.SessionAuthentication",
        "rest_framework.authentication.TokenAuthentication",
    ),
    "TEST_REQUEST_DEFAULT_FORMAT": "json",
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.LimitOffsetPagination",
    "PAGE_SIZE": 100,
    "COERCE_DECIMAL_TO_STRING": False,
}

# log to console, assume the supervisor/system runner will take care of the logs
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {"console": {"class": "logging.StreamHandler"}},
    "loggers": {"": {"handlers": ["console"], "level": "DEBUG"}},
}

CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True
CORS_ALLOW_HEADERS = default_headers + ("content-disposition",)

