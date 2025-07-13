# Deep learning model deploy with Django

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)

**Executive Summary**

This project is a Django-REST API that offers the consumption of a deep learning model using a simple front end. The model adopted in this work is the previous version of an Emotion Classifier trained with audio files of the [RAVDESS dataset](https://zenodo.org/record/1188976#.XvO2WZMza3c). To know more, see [this repository](https://github.com/marcogdepinto/emotion-classification-from-audio-files). 

# How does this work?

**User Journey**

The user journey starts on the index page at ```/index/``` where it is possible to choose if 

1) Upload a new file on the server;
2) Delete a file from the server (WIP);
3) Make a prediction on a file already on the server;

![Picture1](https://github.com/marcogdepinto/Django-Emotion-Classification-Ravdess-API/blob/master/gitmedia/index.png)

Choosing ```Upload your audio file``` the user will be redirected to a modified home page. The user will be asked to pick a file from his computer. The UI will confirm if the operation has been successful. 

![Picture2](https://github.com/marcogdepinto/Django-Emotion-Classification-Ravdess-API/blob/master/gitmedia/fileuploadv2.png)

Choosing ```Make your prediction``` the user will be redirected to a modified home page. In this page, it will be possible to see a list of the files already on the server. Following the path ```media/{filename}``` it will be also possible to listen to the audio file.

![Picture3](https://github.com/marcogdepinto/Django-Emotion-Classification-Ravdess-API/blob/master/gitmedia/fileselectionv2.png)

After clicking on ```Submit```, the user will be redirected to a modified home page that will include the prediction made by the Keras model for the file selected.

![Picture4](https://github.com/marcogdepinto/Django-Emotion-Classification-Ravdess-API/blob/master/gitmedia/predict.png)

# Developers stuff

**DB creation**

PostgreSQL needs to be installed. To facilitate the configuration, I suggest to use a Db manager with UI, like [pgAdmin](https://www.pgadmin.org/). 

After the installation of PostgreSQL, it is possible to use pgAdmin to create a ```django-emotion-classification``` database and a ```App_filemodel``` table.

The ```App_filemodel``` table can be created with the following script:

```
CREATE DATABASE django-emotion-classification;

CREATE USER marco WITH PASSWORD 'test';

CREATE TABLE App_filemodel (
   id INT PRIMARY KEY NOT NULL,
   file TEXT NOT NULL,
   timestamp DATE NOT NULL,
   path TEXT NOT NULL
);

GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA django-emotion-classification TO marco;

ALTER USER marco CREATEDB; -- This is to run the automatic tests, otherwise you will get an "unable to create database" error when running python manage.py test

```

Please note the above script is made with the data available in the ```settings.py```, but it is possible to change it if needed.
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'django-emotion-classification',
        'USER': 'marco',
        'PASSWORD': 'test',
        'HOST': 'localhost',
        'PORT': '',
        'OPTIONS': {'sslmode': 'disable'},
    }
}
```

**How to start the server and try it**

1) ```git clone https://github.com/marcogdepinto/Django-Emotion-Classification-Ravdess-API.git```
2) ```$ pip install -r requirements.txt```
3) Open a terminal window, ```cd``` into the project folder and run ```python manage.py runserver```.

**How to run the tests**

```python manage.py test```

**Other important topics**

The Keras model is stored in the ```models``` folder.

```gitmedia``` folder includes the pictures used for this README.

```media``` folder includes the audio files loaded using the server. 

It is possible to have an overview of the application even without knowing how Django works by looking at the ``App/views.py`` file.

**User Stories**

https://github.com/marcogdepinto/Django-Emotion-Classification-Ravdess-API/projects/2
