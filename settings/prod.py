from .common import *  # noqa: ignore=F405

import os
import raven

DEBUG = False

ALLOWED_HOSTS = [
     "health.aiaudit.org",
     "health.aiaudit.org:443",
     "health.aiaudit.org:8000"
]


CORS_ORIGIN_ALLOW_ALL = True

#CORS_ORIGIN_WHITELIST = (
#    "https://health.aiaudit.org",
#    "https://health.aiaudit.org:8000",
#    "https://health.aiaudit.org:9999",
#    "http://health.aiaudit.org",
#)

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": os.environ.get("RDS_DB_NAME"),
        "USER": os.environ.get("RDS_USERNAME"),
        "PASSWORD": os.environ.get("RDS_PASSWORD"),
        "HOST": os.environ.get("RDS_HOSTNAME"),
        "PORT": os.environ.get("RDS_PORT"),
    }
}

DATADOG_APP_NAME = "EvalAI"
DATADOG_APP_KEY = os.environ.get("DATADOG_APP_KEY")
DATADOG_API_KEY = os.environ.get("DATADOG_API_KEY")

#MIDDLEWARE += ["middleware.metrics.DatadogMiddleware"]  # noqa

INSTALLED_APPS += ("storages", "raven.contrib.django.raven_compat")  # noqa

AWS_STORAGE_BUCKET_NAME = os.environ.get("AWS_STORAGE_BUCKET_NAME")
AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")
AWS_SES_REGION_NAME = os.environ.get("AWS_SES_REGION_NAME")
AWS_SES_REGION_ENDPOINT = os.environ.get("AWS_SES_REGION_ENDPOINT")

# # Amazon S3 Configurations
AWS_S3_CUSTOM_DOMAIN = "ai4h.s3.amazonaws.com"

# static files configuration on S3
STATICFILES_LOCATION = "static"
STATICFILES_STORAGE = "settings.custom_storages.StaticStorage"
STATIC_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, STATICFILES_LOCATION)

# Media files configuration on S3
MEDIAFILES_LOCATION = "media"
MEDIA_URL = "http://%s.s3.amazonaws.com/%s/" % (
    AWS_STORAGE_BUCKET_NAME,
    MEDIAFILES_LOCATION,
)
DEFAULT_FILE_STORAGE = "settings.custom_storages.MediaStorage"

STATIC_URL = "static"

# Media files configuration on S3
MEDIAFILES_LOCATION = "media"
MEDIA_URL = "http://%s.s3.amazonaws.com/%s/" % (
    os.environ.get("AWS_STORAGE_BUCKET_NAME"),
    MEDIAFILES_LOCATION,
)


# Setup Email Backend related settings
#DEFAULT_FROM_EMAIL = "noreply@cloudcv.org"
DEFAULT_FROM_EMAIL = "steffen.vogler@bayer.com"
#EMAIL_BACKEND = "django_ses.SESBackend"
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = os.environ.get("EMAIL_HOST")
EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_HOST_PASSWORD")
EMAIL_HOST_USER = os.environ.get("EMAIL_HOST_USER")
EMAIL_PORT = os.environ.get("EMAIL_PORT")
EMAIL_USE_TLS = os.environ.get("EMAIL_USE_TLS")


# Hide API Docs on production environment
REST_FRAMEWORK_DOCS = {"HIDE_DOCS": True}

# Port number for the python-memcached cache backend.
CACHES["default"]["LOCATION"] = os.environ.get(  # noqa: ignore=F405
    "MEMCACHED_LOCATION"
)  # noqa: ignore=F405

# https://docs.djangoproject.com/en/1.10/ref/settings/#secure-proxy-ssl-header
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = True
SECURE_REDIRECT_EXEMPT = [r'^(?!admin/).*']

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler'
        },
    },
    'loggers': {
        '': {
            'handlers': ['console'],
            'level': 'DEBUG',
        },
    },
}
