from django.conf import settings
from storages.backends.s3boto3 import s3boto3Storage


class StaticStorage(S3boto3Storage):
    location = settings.STATICFILES_LOCATION


class MediaStorage(S3boto3Storage):
    location = settings.MEDIAFILES_LOCATION

