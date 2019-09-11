# Django-rest API to serve an emotion classification deep learning model

Emotion Classification RAVDESS is a project that is able to predict the emotions of a recorded speaker using a deep neural network.

More information about the project can be found in the related repository: https://github.com/marcogdepinto/Emotion-Classification-Ravdess

This repository includes a Django-based API to serve the deep learning model previously trained.
In addition, a simple front end is provided.

# Why I am doing this?

The vision of this project is to show that artificial intelligence applications can be shipped to production, consumed by users and have a real impact.
This is just a research project, but hope it can inspire someone to build something big :)

# How does this work?

## User Journey

The user journey start on the index page at ```/index/``` where it is possible to choose if 

1) Upload a new file on the server;
2) Delete a file from the server (WIP);
3) Make a prediction on a file already on the server;

![Picture1](https://github.com/marcogdepinto/Django-Emotion-Classification-Ravdess-API/blob/master/gitmedia/index.png)

Choosing ```Upload your audio file``` a new window will be prompted. The user will be asked to pick a file from his computer and then will be prompted with a page that will confirm that the upload has been successful.

![Picture2](https://github.com/marcogdepinto/Django-Emotion-Classification-Ravdess-API/blob/master/gitmedia/fileupload.png)

Choosing ```Make your prediction``` a new window will be prompted. In this window, it will be possible to see a list of the files already on the server. Following the path ```media/{filename}``` it will be also possible to listen to the audio file.

![Picture3](https://github.com/marcogdepinto/Django-Emotion-Classification-Ravdess-API/blob/master/gitmedia/fileselection.png)

After clicking on ```Submit```, the user will be redirected to a modified home page that will include the prediction made by the Keras model for the file selected.

![Picture4](https://github.com/marcogdepinto/Django-Emotion-Classification-Ravdess-API/blob/master/gitmedia/predict.png)

# See the App in action!

There is a short demo of the first version on YouTube: https://youtu.be/86HhxTRL3_c

# Developers stuff

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

If you do not know how Django works, you can skip to the ``App/views.py`` file to review the high level logic of the API.

**User Stories**

What is the plan for the future and what it is currently ongoing: https://github.com/marcogdepinto/Django-Emotion-Classification-Ravdess-API/projects/2