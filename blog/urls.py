from django.contrib import admin
from django.urls import path
from blog.views import *
urlpatterns = [
    path("",tryhtml1, name="tryhtml1"),
	path("accueil",accueil),
	path("tryhtml1",tryhtml1),
	path("donnees",insertion_donnees),
	path("van",van),
	path("ip",ip),
	path("comparaison",comparaison),
	path("tir",tir),
]