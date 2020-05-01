"""
Models.py includes the database structure of the application.
"""

from django.db import models
from django.conf import settings
from django.dispatch import receiver
from django.db.models.signals import post_delete


class FileModel(models.Model):
    file = models.FileField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    path = models.FilePathField(path=settings.MEDIA_ROOT, default=settings.MEDIA_ROOT)

    class Meta:	
        unique_together = ['file', 'path']	


@receiver(post_delete, sender=FileModel)
def submission_delete(sender, instance, **kwargs):
    """
    This function is used to delete attachments when a file object is deleted.
    Django does not do this automatically.
    """
    instance.file.delete(False)
