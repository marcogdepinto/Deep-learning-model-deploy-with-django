from django.db import models
from django.conf import settings


class FileModel(models.Model):
    file = models.FileField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    path = models.FilePathField(path=settings.MEDIA_ROOT, default=settings.MEDIA_ROOT)
