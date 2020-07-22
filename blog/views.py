from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

""" Exemple de page non valide au niveau HTML pour que l'exemple soit concis """
    
def tryhtml1(request):
    return render(request, "tryhtml1.html")
def accueil(request):
	return tryhtml1
def insertion_donnees(request):
	return render(request,"donnees.html")
def van(request):
    return render(request,"van.html")
def ip(request):
    return render(request,"ip.html")	
def comparaison(request):
	return render(request,"comparaison.html")
def tir(request):
	return render(request,"tir.html")
