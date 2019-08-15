import os
import keras
import librosa
import logging
import numpy as np
import tensorflow as tf
from .forms import FileForm
from rest_framework import views
from django.conf import settings
from rest_framework import status
from django.shortcuts import render
from App.serialize import FileSerializer
from .functions import handle_uploaded_file
from django.http import HttpResponseRedirect
from rest_framework.response import Response
from django.views.generic import TemplateView
from rest_framework.parsers import MultiPartParser, FormParser


class IndexView(TemplateView):
    template_name = "index.html"
    log = logging.getLogger(__name__)
    log.debug("Debug testing")

    def post(self, request): # TODO: fix, empty file error returned after calling post method
        # if this is a POST request we need to process the form data
        if request.method == 'POST':
            # create a form instance and populate it with data from the request:
            # https://docs.djangoproject.com/en/2.2/ref/forms/api/#binding-uploaded-files
            form = FileForm(request.POST, request.FILES)
            # check whether it's valid:
            if form.is_valid():
                handle_uploaded_file(request.FILES['file'])
                form.save()
                # redirect to a new URL:
                return HttpResponseRedirect('/App/index/')
        # if a GET (or any other method) we'll create a blank form
        else:
            form = FileForm()
        return render(request, 'index.html', {'form': form})


class FileView(views.APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request):
        '''This method is used to Make POST requests to save a file in the media folder'''
        file_serializer = FileSerializer(data=request.data)
        if file_serializer.is_valid():
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
