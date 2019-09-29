"""DjangoRestDeepLearning URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import re_path
from django.views.static import serve
from django.conf import settings
from django.conf.urls import url
from django.conf.urls import include
from django.conf.urls.static import static

from App.views import UploadView
from App.views import FilesList
from App.views import IndexView
from App.views import UploadSuccessView
from App.views import SelectPredFileView
from App.views import SelectFileDelView
from App.views import FileDeleteView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^App/', include('App.urls'), name='App'),
    url('index/', IndexView.as_view(), name='index'),

    # Urls to upload the file and confirm the upload
    url('fileupload/', UploadView.as_view(), name='upload_file'),
    url('upload_success/', UploadSuccessView.as_view(), name='upload_success'),

    # Url to select a file for the predictions
    url('fileselect/', SelectPredFileView.as_view(), name='file_select'),

    # Url to select a file to be deleted and confirm the upload
    url('filedelete/', SelectFileDelView.as_view(), name='file_delete'),
    url('delete_success/(?P<pk>\d+)/$', FileDeleteView.as_view(), name='delete_success'),

    # Url to list all the files in the server
    url('files_list/', FilesList.as_view(), name='files_list'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:

    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
        re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT, }),
    ] + urlpatterns
