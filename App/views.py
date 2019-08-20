import os
import keras
import librosa
import numpy as np
import tensorflow as tf
from App.models import FileModel
from rest_framework import views
from django.conf import settings
from rest_framework import status
from App.serialize import FileSerializer
from rest_framework.response import Response
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from rest_framework.parsers import MultiPartParser, FormParser


class IndexView(TemplateView):
    template_name = 'index.html'


class UploadView(CreateView):
    model = FileModel
    fields = ['file']
    template_name = 'post_file.html'
    success_url = '/upload_success/'


class UploadSuccessView(TemplateView):
    template_name = 'upload_success.html'


class FileView(views.APIView):
    parser_classes = (MultiPartParser, FormParser)

    def upload(self, request):
        '''This method is used to Make POST requests to save a file in the media folder'''
        file_serializer = FileSerializer(data=request.data)
        if file_serializer.is_valid():
            # TODO: implement a check to see if the file is already on the server
            file_serializer.save()
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        raise NotImplementedError # TODO: implement


class Predict(views.APIView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        modelname = 'Emotion_Voice_Detection_Model.h5'
        global graph
        graph = tf.get_default_graph()
        self.loaded_model = keras.models.load_model(os.path.join(settings.MODEL_ROOT, modelname))
        self.predictions = []

    def post(self, request):
        '''This method is used to making predictions on audio files previously loaded with FileView.post'''
        with graph.as_default():
            for entry in request.data:
                filename = entry.pop("filename")
                filepath = str(os.path.join(settings.MEDIA_ROOT, filename))
                data, sampling_rate = librosa.load(filepath)
                try:
                    mfccs = np.mean(librosa.feature.mfcc(y=data, sr=sampling_rate, n_mfcc=40).T, axis=0)
                    x = np.expand_dims(mfccs, axis=2)
                    x = np.expand_dims(x, axis=0)
                    numpred = self.loaded_model.predict_classes(x)
                    self.predictions.append([self.classtoemotion(numpred)])
                except Exception as err:
                    return Response(str(err), status=status.HTTP_400_BAD_REQUEST)

        return Response(self.predictions, status=status.HTTP_200_OK)

    def classtoemotion(self, pred):
        '''

        This method is used to convert the predictions (int) into human readable strings.
        ::pred:: An int from 0 to 7.
        ::output:: A string label

        Example:

        >>> classtoemotion(0) == neutral

        '''

        if pred == 0:
            pred = "neutral"
            return pred
        elif pred == 1:
            pred = "calm"
            return pred
        elif pred == 2:
            pred = "happy"
            return pred
        elif pred == 3:
            pred = "sad"
            return pred
        elif pred == 4:
            pred = "angry"
            return pred
        elif pred == 5:
            pred = "fearful"
            return pred
        elif pred == 6:
            pred = "disgust"
            return pred
        elif pred == 7:
            pred = "surprised"
            return pred
        else:
            return "Prediction out of expected range (1-7)"
