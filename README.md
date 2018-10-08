# Django REST-framework Study Project

This is a simple REST API built with Django REST framework. 
Main focus is how to handle various HTTP requests. 

## How To install
This project assume you've already installed pip on your environment. 

I highly encourage you to install the virutal environment so that you can create an independent environment
for this project. This can keep you out from affecting other projects due to installing anything for this one. 
```
pip3 install virtualenv 
```

Create virtual environment on the same dir where this project root folder is located at. 
Activate the environment

```
virtualenv [name]
source [name]/bin/activate 
```

Get inside of the project folder and install all the dependencies 

```
cd [project folder]
pip3 install -r requirements.txt
```

Run server with following line
```
python3 manage.py runserver
```
## Django Cheatsheet
Creating a new project
django-admin startproject projectname

Add an app to a project
python3 manage.py startapp appname

Starting the server
// In case of c9, you need to add $IP:$PORT at the end of the command
python3 manage.py runserver $IP:$PORT

Creating migrations
python3 manage.py makemigrations

Migrate the database
python3 manage.py migrate

Creating a Super User for the admin panel
python3 manage.py createsuperuserRun 

Collecting static files into one folder
python3 manage.py collectstatic

        
## Function Description


## Built With

* [Django](https://www.djangoproject.com) - Python Web framework
* [Django REST framework](https://www.django-rest-framework.org) - To handle API requests


## Authors

* **Geon Yoon ** - *Initial work* - [GeonYoon](https://github.com/GeonYoon)