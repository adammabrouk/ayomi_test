from django.db import models

# Create your models here.


USERS = [
   {'firstname' : 'adam', 'lastname' : 'mabrouk', 'email' : 'adammabrouk1990@gmail.com', 'password' : '1111',  'phone' : '0665205166', 'adress' : '1 Square Mérimée', 'date' : '06/11/2020'},
   {'firstname' : 'soukaina', 'lastname' : 'mabrouk', 'email' : 'soukaina.mabrouk@gmail.com', 'password' : '2222','phone' : '0752336615', 'adress' : '1 Square Mérimée', 'date' : '06/11/2020'},
   {'firstname' : 'youssef', 'lastname' : 'mabrouk', 'email' : 'youssef.mabrouk@gmail.com', 'password' : '3333','phone' : '0632556235', 'adress' : '1 Square Mérimée', 'date' : '06/11/2020'}
]

class User(models.Model):
    firstname = models.CharField(max_length=50)
    lastname  = models.CharField(max_length=50)
    email     = models.EmailField(max_length=100, unique=True)
    password  = models.CharField(max_length=50)
    phone     = models.CharField(max_length=15)
    adress    = models.CharField(max_length=200)
    date      = models.DateTimeField(auto_now_add=True)
