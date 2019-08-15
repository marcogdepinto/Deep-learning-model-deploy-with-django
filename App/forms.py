from django.forms import ModelForm
from App.models import FileModel


class FileForm(ModelForm):
    # Creating a form that maps to the model: https://docs.djangoproject.com/en/2.2/topics/forms/modelforms/
    class Meta:
        model = FileModel
        fields = ['file']
