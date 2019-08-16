from django.db import models


class FileModel(models.Model):
    file = models.FileField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
