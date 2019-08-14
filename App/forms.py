from django import forms


class FileForm(forms.Form):
    filename = forms.CharField(label='file')
