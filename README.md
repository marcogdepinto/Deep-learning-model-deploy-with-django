# Django-rest API to serve an emotion classification deep learning model

Emotion Classification RAVDESS is a project that is able to predict the emotions of a recorded speaker using a deep neural network.

More information about the project can be found in the related repository: https://github.com/marcogdepinto/Emotion-Classification-Ravdess

This repository includes a Django-based API to serve the deep learning model previously trained.
In addition, a simple front end is provided.

# Why I am doing this?

The vision of this project is to show that artificial intelligence applications can be shipped to production, consumed by users and have a real impact.
This is just a research project, but hope it can inspire someone to build something big :)

# How does this work?

## Backend

The API has two endpoints:
 
 1) http://127.0.0.1:8000/App/upload/
 2) http://127.0.0.1:8000/App/predict/ 
 
Using the `App/upload` endpoint, it is possible to send a file taken from the RAVDESS dataset examples. The file will be serialized and stored in the `media` folder of the server.

![Picture](https://github.com/marcogdepinto/Django-Emotion-Classification-Ravdess-API/blob/master/gitmedia/fileupload.png)
 
Using the `App/predict` endpoint, sending the filename as input in the format shown below the API will return an array with the predictions.

Example `App/predict` input:

```
{"filename" : "01-01-01-01-01-01-01.wav"}
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

![Picture2](https://github.com/marcogdepinto/Django-Emotion-Classification-Ravdess-API/blob/master/gitmedia/predict_n.png)

The model is stored in the ```models``` folder.

The ```templates``` folder will contain a Bootstrap simple UI to interact with the API (work in progress).

If you do not know how Django works, you can skip to the ``App/views.py`` file to review the high level logic of the API.

## Front end

The project includes a simple frontend to query the API, using a web interface instead of dedicated applications or tools like postman.

The front end is still work in progress: below the actual mockup. 

![Picture2](https://github.com/marcogdepinto/Django-Emotion-Classification-Ravdess-API/blob/master/gitmedia/interface2.png)

# Developers stuff

**How to start the server and try it**

1) Install Django and the Django-Rest framework.
2) ```git clone https://github.com/marcogdepinto/Django-Emotion-Classification-Ravdess-API.git```
3) Open a terminal window, ```cd``` into the project folder and run ```python manage.py runserver```.

**How to run the tests**

```python manage.py test```

**Check the user stories**
What is the plan for the future and what is ongoing: https://github.com/marcogdepinto/Django-Emotion-Classification-Ravdess-API/projects/2