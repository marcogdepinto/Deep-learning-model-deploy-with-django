"""
views.py includes the main business logic of the application.
Its role is to manage file upload, deletion and emotion predictions.
"""

import os
from os import listdir
from os.path import join
from os.path import isfile

import keras
import librosa
import numpy as np
import tensorflow as tf
from django.conf import settings
from django.views.generic import DeleteView
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from rest_framework import views
from rest_framework import status
from rest_framework.parsers import FormParser
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer

from App.models import FileModel
from App.serialize import FileSerializer


class IndexView(TemplateView):
    """
    This is the index view of the website.
    """
    template_name = 'index.html'


class UploadView(CreateView):
    """
    This is the view that is used by the user of the web UI to upload a file.
    """
    model = FileModel
    fields = ['file']
    template_name = 'post_file.html'
    success_url = '/upload_success/'


class UploadSuccessView(TemplateView):
    """
    This is the success view of the UploadView class.
    """
    template_name = 'upload_success.html'


class SelectPredFileView(TemplateView):
    """
    This view is used to select a file from the list of files in the server.
    After the selection, it will send the file to the server.
    The server will return the predictions.
    """

    template_name = 'select_file_predictions.html'
    parser_classes = FormParser
    queryset = FileModel.objects.all()

    def get_context_data(self, **kwargs):
        """
        This function is used to render the list of files in the MEDIA_ROOT in the html template.
        """
        context = super().get_context_data(**kwargs)
        media_path = settings.MEDIA_ROOT
        myfiles = [f for f in listdir(media_path) if isfile(join(media_path, f))]
        context['filename'] = myfiles
        return context


class SelectFileDelView(TemplateView):
    """
    This view is used to select a file from the list of files in the server.
    After the selection, it will send the file to the server.
    The server will then delete the file.
    """
    template_name = 'select_file_deletion.html'
    parser_classes = FormParser
    queryset = FileModel.objects.all()

    def get_context_data(self, **kwargs):
        """
        This function is used to render the list of files in the MEDIA_ROOT in the html template.
        """
        context = super().get_context_data(**kwargs)
        media_path = settings.MEDIA_ROOT
        myfiles = [f for f in listdir(media_path) if isfile(join(media_path, f))]
        context['filename'] = myfiles
        return context


class FileView(views.APIView):
    """
    This class contains the method to upload a file interacting directly with the API.
    POST requests are accepted.
    """
    parser_classes = (MultiPartParser, FormParser)
    queryset = FileModel.objects.all()

    def upload(self, request):
        """
        This method is used to Make POST requests to save a file in the media folder
        """
        file_serializer = FileSerializer(data=request.data)
        if file_serializer.is_valid():
            # TODO: implement a check to see if the file is already on the server
            file_serializer.save()
            response = Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            response = Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return response


class FileDeleteView(DeleteView):
    """
    This class contains the method to delete a file interacting directly with the API.
    DELETE requests are accepted.
    """
    # TODO: Fix, still not working
    template_name = 'delete_success.html'
    model = FileModel
    success_url = '/index/'


class DeleteSuccessView(TemplateView):
    """
    This is the success view of the UploadView class.
    """
    template_name = 'delete_success.html'


class Predict(views.APIView):
    """
    This class is used to making predictions.

    Example of input:
    {'filename': '01-01-01-01-01-01-01.wav'}

    Example of output:
    [['neutral']]
    """

    template_name = 'index.html'
    renderer_classes = [TemplateHTMLRenderer]  # Removing this line shows the APIview instead of the template.

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        modelname = 'Emotion_Voice_Detection_Model.h5'
        self.graph = tf.get_default_graph()
        self.loaded_model = keras.models.load_model(os.path.join(settings.MODEL_ROOT, modelname))
        self.predictions = []

    def file_elaboration(self, filepath):
        """
        This function is used to elaborate the file used for the predictions with librosa.
        :param filepath:
        :return: predictions
        """
        data, sampling_rate = librosa.load(filepath)
        try:
            mfccs = np.mean(librosa.feature.mfcc(y=data, sr=sampling_rate,
                                                 n_mfcc=40).T, axis=0)
            training_data = np.expand_dims(mfccs, axis=2)
            training_data_expanded = np.expand_dims(training_data, axis=0)
            numpred = self.loaded_model.predict_classes(training_data_expanded)
            self.predictions.append([self.classtoemotion(numpred)])
            return self.predictions
        except ValueError as err:
            return Response(str(err), status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        """
        This method is used to making predictions on audio files
        loaded with FileView.post
        """
        with self.graph.as_default():
            filename = request.POST.getlist('file_name').pop()
            filepath = str(os.path.join(settings.MEDIA_ROOT, filename))
            predictions = self.file_elaboration(filepath)
            try:
                return Response({'predictions': predictions.pop()})
            except ValueError as err:
                return Response(str(err), status=status.HTTP_400_BAD_REQUEST)
        return Response(predictions, status=status.HTTP_200_OK)

    @staticmethod
    def classtoemotion(pred):
        """
        This method is used to convert the predictions (int) into human readable strings.
        ::pred:: An int from 0 to 7.
        ::output:: A string label

        Example:
        classtoemotion(0) == neutral
        """

        label_conversion = {'0': 'neutral',
                            '1': 'calm',
                            '2': 'happy',
                            '3': 'sad',
                            '4': 'angry',
                            '5': 'fearful',
                            '6': 'disgust',
                            '7': 'surprised'}

        for key, value in label_conversion.items():
            if int(key) == pred:
                label = value
        return label
