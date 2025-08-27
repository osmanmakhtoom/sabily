from datetime import timedelta
from pathlib import Path

import environ
import sentry_sdk.utils
from pytimeparse import parse
from sentry_sdk.integrations.celery import CeleryIntegration
from sentry_sdk.integrations.django import DjangoIntegration
from sentry_sdk.integrations.redis import RedisIntegration

# === Paths and Environment ===
BASE_DIR = Path(__file__).resolve().parent.parent.parent

env = environ.Env()
env.read_env(BASE_DIR / ".env")

# === Core Settings ===
SECRET_KEY = env.str("SECRET_KEY")
DEBUG = env.bool("DEBUG", default=False)
ALLOWED_HOSTS = env.list("ALLOWED_HOSTS", default=[])

# === Applications ===
DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

THIRD_PARTY_APPS = [
    "drf_yasg",
    "rest_framework",
    "rest_framework_simplejwt",
    "rest_framework_simplejwt.token_blacklist",
    "corsheaders",
    "django_filters",
    "phonenumber_field",
    "django_celery_beat",
]

LOCAL_APPS = [
    "core",
    "account",
    "app",
    "blog",
    "events",
    "site_settings",
    "quran",
    "zakat",
    "hadith",
    "salah",
    "sawm",
    "knowledge",
    "community",
    "charity",
    "library",
    "books_service",
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

# === Middleware ===
MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# === URL & WSGI ===
ROOT_URLCONF = "core.urls.api"
WSGI_APPLICATION = "core.wsgi.application"

# === User Model ===
AUTH_USER_MODEL = "account.User"

# === Templates ===
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

# === Database & Caching ===
DATABASES = {"default": env.db()}
CACHES = {"default": env.cache()}

# === Password Validators ===
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# === Localization ===
LANGUAGE_CODE = "fa-IR"
TIME_ZONE = "Asia/Tehran"
USE_I18N = True
USE_TZ = True

# === Static & Local & Media Files ===
STATIC_URL = "static/"
STATIC_ROOT = BASE_DIR / "static"
MEDIA_URL = "media/"
MEDIA_ROOT = BASE_DIR / "media"
LOCALE_PATHS = [
    BASE_DIR.joinpath("locale"),
]

# === Auto Field ===
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# === DRF Configuration ===
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ],
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.AllowAny",
    ],
    "DEFAULT_RENDERER_CLASSES": [
        "rest_framework.renderers.JSONRenderer",
        "rest_framework.renderers.BrowsableAPIRenderer",
    ],
    "DEFAULT_PARSER_CLASSES": [
        "rest_framework.parsers.JSONParser",
        "rest_framework.parsers.MultiPartParser",
        "rest_framework.parsers.FormParser",
    ],
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "PAGE_SIZE": 100,
    "DEFAULT_VERSIONING_CLASS": "rest_framework.versioning.NamespaceVersioning",
    "DEFAULT_VERSION": "v1",
    "ALLOWED_VERSIONS": ("v1", "v2"),
    "DEFAULT_SCHEMA_CLASS": "rest_framework.schemas.openapi.AutoSchema",
}

# === CORS ===
CORS_ORIGIN_ALLOW_ALL = env.bool("CORS_ORIGIN_ALLOW_ALL", default=False)
CORS_ALLOWED_ORIGINS = env.list("CORS_ALLOWED_ORIGINS", default=[])
CORS_ALLOW_CREDENTIALS = True

# === SENTRY ===
sentry_sdk.utils.MAX_STRING_LENGTH = 4096
SENTRY_DSN = env.str("SENTRY_DSN")
SENTRY_SAMPLE_RATE = env.float("SENTRY_SAMPLE_RATE", 1.0)
SENTRY_TRACES_SAMPLE_RATE = env.float("SENTRY_TRACES_SAMPLE_RATE", 1.0)
SENTRY_PROFILES_SAMPLE_RATE = env.float("SENTRY_PROFILES_SAMPLE_RATE", 1.0)
SENTRY_OPTS = {
    "integrations": [CeleryIntegration(), DjangoIntegration(), RedisIntegration()],
    "environment": env.str("APP_ENV", None),
    "sample_rate": SENTRY_SAMPLE_RATE,
    "traces_sample_rate": SENTRY_TRACES_SAMPLE_RATE,
    "profiles_sample_rate": SENTRY_PROFILES_SAMPLE_RATE,
    "send_default_pii": True,
    "max_request_body_size": "always",
    "max_value_length": 1024 * 256,
}

sentry_sdk.init(SENTRY_DSN, release=env.str("APP_VERSION"), **SENTRY_OPTS)


def parse_timedelta(value, default):
    if isinstance(value, timedelta):
        return value
    if value is None:
        return default
    seconds = parse(value)
    if seconds is None:
        return default
    return timedelta(seconds=seconds)


# === JWT ===
SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": parse_timedelta(
        env("ACCESS_TOKEN_LIFETIME"), default=timedelta(minutes=60)
    ),
    "REFRESH_TOKEN_LIFETIME": parse_timedelta(
        env("REFRESH_TOKEN_LIFETIME"), default=timedelta(days=1)
    ),
}

SWAGGER_USE_COMPAT_RENDERERS = False
