# Django REST API to serve Emotion Classification RAVDESS

Emotion Classification RAVDESS is a project that is able to predict the emotions of a recorded speaker using a deep neural network.

More information about the project can be found in the related repository: https://github.com/marcogdepinto/Emotion-Classification-Ravdess

This repository includes a Django-based API to serve the deep learning model previously trained.

 **How does this work?**
 
 The API has two endpoints:
 
 1) http://127.0.0.1:8000/file/upload/
 2) http://127.0.0.1:8000/App/predict/ 
 
Using the `file/upload` endpoint, it is possible to send a file taken from the RAVDESS dataset examples. The file will be serialized and stored in the `media` folder of the server.

![Picture](https://github.com/marcogdepinto/Django-Emotion-Classification-Ravdess-API/blob/master/gitmedia/fileupload.png)
 
Using the `App/predict` endpoint, sending the filename as input in the format shown below the API will return an array with the predictions.

Example `App/predict` input:

```
[
{"filename" : "01-01-01-01-01-01-01.wav"}
]
```
Example `App/predict` output:
```
HTTP 200 OK
Allow: POST, OPTIONS
Content-Type: application/json
Vary: Accept

[
    [
        "neutral"
    ]
]
```

![Picture2](https://github.com/marcogdepinto/Django-Emotion-Classification-Ravdess-API/blob/master/gitmedia/predict.png)

The model is stored in the ```models``` folder.

The ```templates``` folder will contain a Bootstrap simple UI to interact with the API (work in progress).

If you do not know how Django works, you can skip to the ``App/views.py`` file to review the high level logic of the API.

**How to start the server and try it**

1) Install Django and the Django-Rest framework.
2) ```git clone https://github.com/marcogdepinto/Django-Emotion-Classification-Ravdess-API.git```
3) Open a terminal window, ```cd``` into the project folder and run ```python manage.py runserver```.
 