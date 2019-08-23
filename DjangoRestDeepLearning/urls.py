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
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path

from App.views import UploadView, UploadSuccessView, IndexView, SelectPredFileView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^App/', include('App.urls'), name="App"),
    url('index/', IndexView.as_view(), name='index'),

    # Urls to upload the file and confirm the upload
    path('fileupload/', UploadView.as_view(), name='upload_file'),
    url('upload_success/', UploadSuccessView.as_view(), name='upload_success'),

    # Urls to select a file for the predictions
    path('fileselect/', SelectPredFileView.as_view(), name='file_select'),
]

if settings.DEBUG:

    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
