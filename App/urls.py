"""
Urls.py includes the url configurations of the application.
"""

from django.conf.urls import url

from App.views import Predict
from App.views import FileView
from App.views import FileDeleteView

app_name = 'App'

urlpatterns = [
    url(r'^predict/$', Predict.as_view(), name='APIpredict'),
    url(r'^upload/$', FileView.as_view(), name='APIupload'),
    url(r'^delete/$', FileDeleteView.as_view(), name='APIdelete'),
]
