from App.views import Predict, FileView
from django.conf.urls import url

app_name = 'App'

urlpatterns = [
    url(r'^predict/$', Predict.as_view(), name="APIpredict"),
    url(r'^upload/$', FileView.as_view(), name='APIupload'),
]


