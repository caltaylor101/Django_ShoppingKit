# Django_ShoppingKit
The settings.py file recently commited will allow someone to run this on their machine locally. 
Python 3.8.5 is recommended to run this, but Python 3.7 - 3.9 should work. 
Create a PostgresQL database with:
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'NewData',
        'USER': 'postgres',
        'PASSWORD': 'password',
        'HOST': '127.0.0.1',
        'PORT': '5432'
    }
}
Pip install from the requirements.txt file. 
Edit the settings.py file for your database settings. 
