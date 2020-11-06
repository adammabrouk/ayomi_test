from django.shortcuts import render
from django.http      import HttpResponse
from .models          import USERS
# Create your views here.

# TODO : add imports for user Model
# TODO : add views for Login / Register / Show details

def index(request):
    message = "Hello World"
    return HttpResponse(message)


def register(request):
    message = "Hello World"
    return HttpResponse(message)

def login(request):
    message = "Hello World"
    return HttpResponse(message)


def details(request, user_id):

    user_id = int(user_id)
    user    = USERS[user_id]

    message  = "<li>First Name : {}</li>".format(user['firstname'])
    message += "<li>Last Name  : {}</li>".format(user['lastname'])
    message += "<li>Email      : {}</li>".format(user['email'])
    message += "<li>Phone      : {}</li>".format(user['phone'])
    message += "<li>Adress     : {}</li>".format(user['adress'])

    message = "<ul>{}</ul>".format(message)

    return HttpResponse(message)
