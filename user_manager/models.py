from django.db import models

# Create your models here.

class User(models.Model):
    """
    Classe pour représenter le modèle de l'utilisateur afin de pouvoir utiliser l'ORM Django
    """

    firstname = models.CharField(max_length=50)
    lastname  = models.CharField(max_length=50)
    email     = models.EmailField(max_length=100, unique=True)
    password  = models.CharField(max_length=50)
    phone     = models.CharField(max_length=15)
    adress    = models.CharField(max_length=200)
    date      = models.DateTimeField(auto_now_add=True)
