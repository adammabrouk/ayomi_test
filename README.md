# Test Ayomi Django 

Dans ce répertoire, j'ai mis à disposition le code source demandé pour le test Django qui permet de réaliser les fonctionnalités suivantes : 

* Avoir une page permettant à un utilisateur de se connecter.
* Une fois connecté, l'utilisateur accède à une page pour afficher / modifier ses informations.
* En cliquant sur "Modifier ses informations", on veut avoir une modale qui s'ouvre.
* Dans cette modale,  on veut un input permettant de modifier son adresse email, ainsi qu'un bouton "enregistrer". A l'appui de ce bouton, l'adresse email sera modifiée dans la base de données et sur la page principale sans rechargement de la page.
* Le code python doit être écrit en Orienté Objet.
* On utilisera Django, Python et Bootstrap
* On utilisera Docker pour le containériser.

Ce répértoire est réparti de la façon suivante : 

```
├── ayomi                    | Dossier principal du projet django
│   ├── asgi.py
│   ├── __init__.py
│   ├── __pycache__
│   ├── settings.py          | Définition des paramètres du projets
│   ├── urls.py              | Définition des routes principales du projet
│   └── wsgi.py
├── db.sqlite3               | Fichier contenant la base de données en sqlite3
├── Dockerfile               | Dockerfile permettant de construire l'image docker du projet à partir du code source
├── manage.py               
├── README.md
├── requirements.txt         | Bibliothèques prérequises python
└── user_manager             | Dossier de l'application qui gère la connexion des utilisateurs
    ├── admin.py
    ├── apps.py
    ├── handlers.py          | Délarations des classes principales qui gèrent la logique de l'application
    ├── __init__.py
    ├── migrations
    ├── models.py            | Déclaration du modèle User utilisé pour faciliter la lecture / enregistrement dans la BDD
    ├── __pycache__
    ├── static               | Dossier qui contient les fichiers statiques ( CSS / JS / images )
    ├── templates            | Dossiers qui contient les gabarits utilisés dans l'application de gestionnaire des utilisateurs
    ├── tests.py
    ├── urls.py              | Définition des routes de l'application
    └── views.py             | Définition des vues de l'application    
```

Pour exécuter le projet, vous pouvez procéder de deux façons : 

## Utilisation de l'image docker à partir du DockerHub

Téléchargez l'image adammabrouk/ayomi_test_django_adam:latest depuis le DockerHub avec la commande : 

```bash
$ docker pull adammabrouk/ayomi_test_django_adam:latest
```

Ensuite demarrez le container avec la commande 

```bash
$ sudo docker run -p 8000:8000 -i -t adammabrouk/ayomi_test_django_adam:latest
```

## Reconstruction de l'image à partir du code

```bash
$ git clone https://github.com/adammabrouk/ayomi_test.git
$ cd ayomi_test/
$ sudo docker build -t ayomi_test_django_adam .
```

Une fois avoir construit l'image ayomi_test_django_adam vous pouvez démarrer le container en utilisant la commande

```bash
$ sudo docker run -p 8000:8000 -i -t ayomi_test_django_adam
```
## Accès au site 

Pour accéder au site web, dans votre navigateur visitez l'adresse :

```
http://127.0.0.1:8000/
```
Ou bien l'adresse suivante 

```
http://127.0.0.1:8000/user_manager/login
```



