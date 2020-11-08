from django.shortcuts import render, redirect
from django.http      import HttpResponse
from .models          import User
from django.template  import loader
from django.urls      import reverse
from django.http      import JsonResponse
from .handlers        import RegisterHandler, LoginHandler, SessionHandler, MailChangeHandler

def index(request):
    return redirect('/user_manager/login')

def register(request, flag = ''):
    """
    Vue permettant de rediriger vers la page Sign up
    """
    if request.session.get('user'):
        # Si l'utilisateur est déja connecté il est envoyé sur la route /details
        return redirect('/user_manager/details')
    else:
        # Sinon, ouverture de la page d'enregistrement
        template = loader.get_template('user_manager/register.html')
        context  = { 'flag' : flag}
        return HttpResponse(template.render(context, request=request))

def login(request, flag = ''):
    """
    Vue permettant de retourner la page Login
    """
    if request.session.get('user'):
        # Si l'utilisateur est déja connecté il est envoyé sur la route /details
        return redirect('/user_manager/details')
    else:
        # Sinon, ouverture de la page de Log in
        template = loader.get_template('user_manager/login.html')
        context  = {'flag' : flag}
        return HttpResponse(template.render(context, request=request))

def verify(request):
    """
    Vue permettant de vérifier les informations envoyé par le formulaire de création de compte
    """
    if request.method == 'POST':
        # Instanciation du gestionnaire d'enregistrement
        handler   = RegisterHandler()
        # Collecte des champs du formulaire
        handler.storeFields(request)
        # Verification d'existence d'utilisateur
        user      = handler.checkExistingUser()
        if not user.exists():
            # Si l'utilisateur n'existe pas, on l'ajoute a la base de
            user = handler.addUser()
            # Retourner vers le login avec message OK
            return redirect('/user_manager/login/1')
        else :
            # Retourner vers le register avec message qui montre que user déja été créé
            return redirect('/user_manager/register/2')

def verify_login(request):
    """
    Vue permettant de vérifier les informations envoyés par le formulaire de Log In
    """
    if request.method == 'POST':
        # Instanciation du gestionnaire d'authentification
        handler  = LoginHandler()
        # Collecte des champs du formulaire
        handler.storeFields(request)
        # Verification de la présence de l'utilisateur avec le bon email / mot de pass
        user = handler.checkLogin()

        if user.exists():
            # Si l'utilisateur existe, on récupère ses information
            user      = handler.getUser()
            # Creation d'une session pour se rappeler de l'utilisateur ( Stockée dans une bdd)
            SessionHandler.createSession(user,request)
            # Redirection ver la page de détails
            return redirect("/user_manager/details")
        else:
            # Si l'utilisateur n'existe pas, redirection vers la page de login avec code erreur
            return redirect('/user_manager/login/2')


def details(request):
    """
    Vue qui présente les détails de l'utilisateur
    """
    if request.session.get('user'):
        user     = request.session['user']
        context  = {'user' : user}
        template = loader.get_template('user_manager/details.html')
        return HttpResponse(template.render(context, request=request))

    else:
        return redirect('/user_manager/login')

def post_mail(request):
    """
    Vue permettant de gérer une requete AJAX pour changer le mail de l'utilisateur
    """
    # Vérification si la requete est de Type AJAX avec une méthode POST
    if request.is_ajax and request.method == "POST":
        if request.POST.get("form-new-mail"):
            # Récupération de la nouvelle adresse mail et application des changements dans la BDD
            new_mail = MailChangeHandler.changeEmail(request)
            return JsonResponse({"new_mail" : new_mail}, status = 200)
        else:
            return JsonResponse({"error": form.errors}, status=400)

    return JsonResponse({"error": ""},status = 400)

def disconnect(request):
    """
    Vue permettant de gérer la déconnexion de l'utilisateur
    """
    if request.session.get('user'):
        # Suppression de la session
        SessionHandler.deleteSession(request)
        return redirect("/user_manager/login")
    else:
        return redirect("/user_manager/login")
