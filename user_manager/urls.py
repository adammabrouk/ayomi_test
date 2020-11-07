from django.urls import path
from django.conf.urls import include, url

from . import views

urlpatterns = [
        path('', views.index),
        path('login/', views.login),
        path('register/', views.register),
        path('login/<flag>', views.login),
        path('register/<flag>', views.register),
        path('details/', views.details),
        path('verify/', views.verify),
        path('verify_login/', views.verify_login),
        path('disconnect/', views.disconnect),
        path('post_mail/', views.post_mail, name="post_mail")
        ]
