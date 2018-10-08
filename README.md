# Django REST-framework Study Project

This is a simple REST API built with Django REST framework. 
Main focus is how to handle various HTTP requests on back-end side. 
Registeration, Login, postings are available through each endpoints. 
By using JWT(JSON Web Token), we securely get the identity of the client.
The best part is that there is no connection between the the auth-server 
and the rest of the servers other than the pre-defined public key.
Customize permission classes can individually authorize different-status-user by thier status. 
Also, customize data queries formed by using tailored serializer classes. 
You can do automated testing as well without any need of writing lines of code. 

## How To install
Make sure you have following software installed in your system. 
* Python3
* pip3

I highly encourage you to install the virutal environment so that you can create an independent environment
for this project. This can keep you out from affecting other projects by installing anything for this. 
```
pip3 install virtualenv 
```

Create virtual environment on the same dir where this project root folder is located at. 
Activate the environment

```
virtualenv [name]
source [name]/bin/activate 
```
Create project folder and clone the repository inside of it.
```
mkdir [project-name]
cd [project-name]
git clone https://github.com/GeonYoon/django-rest.git
```

Install all the dependencies for the project.

```
cd [project folder]
pip3 install -r requirements.txt
```

I used PostgreSQL for my database. Therefore, you need to install and run it. 
```
sudo apt-get install postgresql postgresql-contrib
sudo service postgresql start
```

Customize DATABASES section in setting.py
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': '[YOUR_DB_NAME]',
        'USER' : 'postgres',
        'PASSWORD' : '[YOUR_PASSWORD]',
        'HOST':'localhost',
        'PORT':'5432'
    }
}
```
Create your own super user for /admin
```
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser [name] 
```

Run server with following line
```
python3 manage.py runserver
```

You can run local tests by following line
```
python3 manage.py test 
```
        
## API endpoints
```
List of available API (browseable) at /api
* /admin/                   ---> admin page

* /api/auth/                ---> Login 
* /api/auth/register/       ---> Register
* /api/auth/jwt/            ---> Obtain JWT 
* /api/auth/jwt/refresh     ---> refresh JWT

* /api/user/<username>      ---> User Detail View
* /api/user/<status>        ---> User Status API View

* /api/status/              ---> Status API View
* /api/status/<id>/         ---> Status API Detail View
```

## Django Cheatsheet
```
Creating a new project :
django-admin startproject projectname

Add an app to a project : 
python3 manage.py startapp appname

Starting the server : 
// In case of c9, you need to add $IP:$PORT at the end of the command
python3 manage.py runserver $IP:$PORT

Creating migrations:
python3 manage.py makemigrations

Migrate the database : 
python3 manage.py migrate

Creating a Super User for the admin panel : 
python3 manage.py createsuperuserRun 

Collecting static files into one folder : 
python3 manage.py collectstatic
```


## Built With

* [Django](https://www.djangoproject.com) - Python Web framework
* [Django REST framework](https://www.django-rest-framework.org) - To handle API requests
* [PostgreSQL](https://www.postgresql.org) - Database

## Authors

* **Geon Yoon ** - *Initial work* - [GeonYoon](https://github.com/GeonYoon)