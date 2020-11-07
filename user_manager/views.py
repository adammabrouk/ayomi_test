from django.shortcuts import render, redirect
from django.http      import HttpResponse
from .models          import USERS
from .models          import User
from django.template  import loader
from django.urls      import reverse
from django.http      import JsonResponse

from datetime import datetime
# Create your views here.

# TODO : add imports for user Model
# TODO : add views for Login / Register / Show details

def index(request):
    message = "Hello World"
    return HttpResponse(message)


def register(request, flag = ''):
    #message = "Hello World"
    template = loader.get_template('user_manager/register.html')
    context  = { 'flag' : flag}
    return HttpResponse(template.render(context, request=request))

def login(request, flag = ''):
    #message = "Hello World"
    template = loader.get_template('user_manager/login.html')
    context  = {'flag' : flag}
    return HttpResponse(template.render(context, request=request))





def verify(request):

    if request.method == 'POST':

        firstname = request.POST.get('form-first-name')
        lastname  = request.POST.get('form-last-name')
        email     = request.POST.get('form-email')
        password  = request.POST.get('form-password')
        phone     = request.POST.get('form-phone')
        adress    = request.POST.get('form-adress')

        user = User.objects.filter(email=email)


        if not user.exists():
            # Si l'utilisateur n'existe pas, on l'ajoute a la base de d
            user = User.objects.create(
                firstname = firstname,
                lastname  = lastname,
                email     = email,
                password  = password,
                phone     = phone,
                adress    = adress
            )
            # Retourner vers le login avec message OK
            return redirect('/user_manager/login/1')


        else :
            # Retourner vers le register avec message qui montre que user déja été créé
            return redirect('/user_manager/register/2')

    return HttpResponse(message)

def verify_login(request):

    # TODO : get forms params from POST request
    if request.method == 'POST':

        email    = request.POST.get('form-username')
        password = request.POST.get('form-password')


        try:
            # If user exists
            # TODO : Search for user using email in database [DOne]
            user     = User.objects.get(email = email, password = password)


            # TODO : if user exists, => log him Else redirect to login page with code 2
                                        # TODO : Create a session for user
                                            # Create token

            request.session['user']     =  {"user_id"   : user.id,
                                            "firstname" : user.firstname,
                                            "lastname"  : user.lastname,
                                            "date"      : user.date.strftime("%d/%m/%Y"),
                                            "email"     : user.email ,
                                            "phone"     : user.phone ,
                                            "adress"    : user.adress }

            message = "Session created"


            return redirect("/user_manager/details")


        except:
            # If user doesn't exist
            return redirect('/user_manager/login/2')



def details(request):
    if request.session.get('user'):
        user     = request.session['user']
        context  = {'user' : user}
        template = loader.get_template('user_manager/details.html')
        return HttpResponse(template.render(context, request=request))

    else:
        return redirect('/user_manager/login')

def post_mail(request):
    # request should be ajax and method should be POST.
    if request.is_ajax and request.method == "POST":
        # get the form data
        if request.POST.get("form-new-mail"):

            new_mail = request.POST['form-new-mail']
            user_id  = request.session['user']['user_id']
            user = User.objects.get(id = int(user_id))

            user.email = new_mail
            user.save()

            request.session['user']     =  {"user_id"   : user.id,
                                            "firstname" : user.firstname,
                                            "lastname"  : user.lastname,
                                            "date"      : user.date.strftime("%d/%m/%Y"),
                                            "email"     : user.email ,
                                            "phone"     : user.phone ,
                                            "adress"    : user.adress }

            return JsonResponse({"new_mail" : new_mail}, status = 200)

        else:
            # some form errors occured.
            return JsonResponse({"error": form.errors}, status=400)

    # some error occured
    return JsonResponse({"error": ""},status = 400)

def disconnect(request):
    if request.session.get('user'):
        del request.session['user']
        return redirect("/user_manager/login")
    else:
        return redirect("/user_manager/login")
