from rest_framework import serializers
from .models import File


class FileSerializer(serializers.ModelSerializer):

    class Meta:
        model = File
        fields = ('file', 'timestamp')
