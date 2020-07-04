# SentimentClassifierWebService
Django REST API for making calls to my C-LSTM Model (Zhou Et Al. 2015) for multi-class (Positive, Neutral, Negative) sentiment classification trained on 1M+ Amazon Movies &amp; T.V Show reviews

## Getting Started
These instructions will help you get the Django project up and running on your local machine for making calls to the model, development and testing. 

## Prequisites 
### Git LFS
I use Git LFS to store the copy of the .h5 keras model file and a JSON file for the Keras tokenizer used during the preprocessing stage. If you have brew installed 
you can dowload and install it using these commands before cloning this repo.
```
$ brew install git-lfs

$ git lfs install
```
[Git LFS](https://git-lfs.github.com/) - for more instructions 

## Installing 
Once you've cloned this repo on your local machine. You can cd into the SentimentClassifierWebService directory and activate the python(3.7) virtual environment
with all of it's dependencies. 
```
$ cd SentimentClassifierWebService/

$ source venv/bin/activate
```
There's also a requirements.txt file in the server directory that you can use check if all the dependencies are installed in case you run into any issues later.
```
$ pip install -r server/requirements.txt
```
## Testing
Once you've activated the virtual environment, you can do a quick sanity check by running the test file. The tests check that the model is successfully 
registered when the server is run and it also makes a call to the model using a single static JSON object and validates and prints the output. You can 
find the test at server/apps/ml/tests.py in case you wanna change the input and run your own custom tests. 
```
$ cd server/

$ python manage.py test apps.ml.tests
```
It may take a few seconds to get the server up and running and get the model registered. This happens only once when the server is run and test time does not 
indicate the time it takes to make a call to the model. That is much faster. You'll see a few TensorFlow warnings as I am using an older version of TensorFlow 
and Keras that behave better with Django. If the test ran successfully, this is what you would see at the end of your terminal.
```
System check identified no issues (0 silenced).
{'Label': 'Negative', 'Negative': 0.94066143, 'Neutral': 0.03895902, 'Positive': 0.02037953, 'Status': 'OK'}
..
----------------------------------------------------------------------
Ran 2 tests in 21.152s

OK
Destroying test database for alias 'default'...
```

## Running the Django app
Once you've made sure everything is working as it is supposed to, you can go ahead and delploy the app on your local machine. To do that cd into the server 
if you haven't already and run it with the following commands. 
```
$ cd server/

$ python manage.py runserver
```
This will take a few seconds and you'll see the same output you did while running the tests. Once the server is up and running, you'll see the local address
it's running at at the end of the terminal output. You can go to that address in your browser which will take you to the API root directory of the Django app.
You can access and view the following JSON objects through the root directory.
 * Endpoints - The endpoint associated with the model.
 * Model - The model object and it's code.
 * Status - The status associated with the model
 * Requests - All JSON requests made to the model 
 <br>
 You can take a look in the server/apps/endpoints/models.py file for more details on all those objects. 
 
 
