from django.urls import path
from App.views import Predict, FileView, IndexView
from django.conf.urls import url


app_name = 'App'

urlpatterns = [
    path('index/', IndexView.as_view(), name="index"),
    url(r'^predict/$', Predict.as_view(), name="predict"),
    url(r'^upload/$', FileView.as_view(), name='file-upload')
]