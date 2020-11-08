from .models     import User
from  datetime   import datetime


class RegisterHandler():
    """
    Classe permettant de gérer les règles d'enregistrement d'un nouveau utilisateur
    """
    def storeFields(self, request):
        # Méthode pour récupérer les données fournies par le formulaire
        self.firstname = request.POST.get('form-first-name')
        self.lastname  = request.POST.get('form-last-name')
        self.email     = request.POST.get('form-email')
        self.password  = request.POST.get('form-password')
        self.phone     = request.POST.get('form-phone')
        self.adress    = request.POST.get('form-adress')

    def checkExistingUser(self):
        # Méthode pour vérifier l'existence d'un utilsateur dans la BDD
        return User.objects.filter(email= self.email)

    def addUser(self):
        # Méthode pour ajouter un utilsateur dans la BDD
        return User.objects.create(
            firstname = self.firstname,
            lastname  = self.lastname,
            email     = self.email,
            password  = self.password,
            phone     = self.phone,
            adress    = self.adress
        )

class LoginHandler():
    """
    Classe permettant de gérer les règles d'authentification d'un nouveau utilisateur
    """
    def storeFields(self, request):
        # Méthode pour récupérer les champs depuis le formulaire
        self.email    = request.POST.get('form-username')
        self.password = request.POST.get('form-password')

    def checkLogin(self):
        # Méthode pour vérifier l'existence de l'utilisateur (email et mot de pass)
        return User.objects.filter(email = self.email, password = self.password)

    def getUser(self):
        # Méthode pour récupérer l'utilisateur depuis la base de données
        return User.objects.get(email = self.email, password = self.password)



class SessionHandler():
    """
    Classe permettant de gérer les sessions
    """
    def createSession(user, request):
        # Méthode pour créer une nouvelle session pour un utilisateur venant de se connecter
        request.session['user']     =  {"user_id"   : user.id,
                                        "firstname" : user.firstname,
                                        "lastname"  : user.lastname,
                                        "date"      : user.date.strftime("%d/%m/%Y"),
                                        "email"     : user.email ,
                                        "phone"     : user.phone ,
                                        "adress"    : user.adress }

    def deleteSession(request):
        # Méthode pour la suppression de session
        del request.session['user']


class MailChangeHandler():
    """
    Classe permettant de gérer les règles de changement de mail
    """
    def changeEmail(request):
        # Méthode permettant de changer l'adresse mail pour l'utilisateur connecté
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

        return new_mail
