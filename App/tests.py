from django.test import TestCase
from rest_framework.request import Request
from rest_framework.parsers import MultiPartParser, FormParser
from django.core.files.uploadedfile import SimpleUploadedFile
from rest_framework.test import APIRequestFactory


class TestFileUpload(TestCase):

    def testupload(self):
        """
        Ensure request.POST returns no content for POST request with file content.
        """
        factory = APIRequestFactory()
        upload = SimpleUploadedFile("file.txt", b"file_content")
        request = Request(factory.post('App/upload', {'upload': upload}))
        request.parsers = (FormParser(), MultiPartParser())
        assert list(request.POST) == []
        assert list(request.FILES) == ['upload']


class TestPredict(TestCase):

    def testupload(self):
        # TODO: implement
        raise NotImplementedError

