from django.conf import settings
from storages.backends.S3boto3 import S3boto3Storage


class StaticStorage(S3boto3Storage):
    location = settings.STATICFILES_LOCATION


class MediaStorage(S3boto3Storage):
    location = settings.MEDIAFILES_LOCATION
