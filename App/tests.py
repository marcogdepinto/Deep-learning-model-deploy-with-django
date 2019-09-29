"""
tests.py includes all the tests of the application.
"""

import os

from django.test import TestCase
from rest_framework.request import Request
from rest_framework.test import APIRequestFactory
from rest_framework.parsers import MultiPartParser, FormParser
from django.core.files.uploadedfile import SimpleUploadedFile

from App.views import Predict
from App.forms import FileForm


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

    def testmodeldir(self):
        """
        Ensure a directory for the models exists
        """
        directory_path = 'models/'
        assert os.path.exists(directory_path)

    def testfilemodel(self):
        """
        Ensure a model exists in the related directory
        """
        model_name_dir = 'models/Emotion_Voice_Detection_Model.h5'
        assert os.path.isfile(model_name_dir)

    def testclasstoemotion(self):
        """
        Ensure classtoemotion function is converting int to labels properly
        """
        self.assertEqual(Predict.classtoemotion(0), "neutral")
        self.assertEqual(Predict.classtoemotion(1), "calm")
        self.assertEqual(Predict.classtoemotion(2), "happy")
        self.assertEqual(Predict.classtoemotion(3), "sad")
        self.assertEqual(Predict.classtoemotion(4), "angry")
        self.assertEqual(Predict.classtoemotion(5), "fearful")
        self.assertEqual(Predict.classtoemotion(6), "disgust")
        self.assertEqual(Predict.classtoemotion(7), "surprised")


class TestTemplates(TestCase):

    def testtemplatedir(self):
        """
        Ensure a templates folder exists
        """
        directory_path = 'App/templates/'
        assert os.path.exists(directory_path)

    def testindex(self):
        """
        Ensure a index template exists
        """
        file_name_dir = 'App/templates/index.html'
        assert os.path.isfile(file_name_dir)

    def testpost(self):
        """
        Ensure a post_file template exists
        """
        file_name_dir = 'App/templates/post_file.html'
        assert os.path.isfile(file_name_dir)

    def testuploadsuccess(self):
        """
        Ensure a upload_success template exists
        """
        file_name_dir = 'App/templates/upload_success.html'
        assert os.path.isfile(file_name_dir)

    def testselectfile(self):
        """
        Ensure a select_file_predictions template exists
        """
        file_name_dir = 'App/templates/select_file_predictions.html'
        assert os.path.isfile(file_name_dir)

    def testdeletefile(self):
        """
        Ensure a select_file_predictions template exists
        """
        file_name_dir = 'App/templates/select_file_deletion.html'
        assert os.path.isfile(file_name_dir)

    def testdeletesuccess(self):
        """
        Ensure a delete_success template exists
        """
        file_name_dir = 'App/templates/delete_success.html'
        assert os.path.isfile(file_name_dir)

    def testfileslist(self):
        """
        Ensure a upload_success template exists
        """
        file_name_dir = 'App/templates/files_list.html'
        assert os.path.isfile(file_name_dir)


class TestFileUploadForm(TestCase):

    def testfileform(self):
        """
        Ensure FileForm is valid
        """
        form_data = {'file': '123.txt'}
        form = FileForm(data=form_data)
        self.assertTrue(form.is_valid())
