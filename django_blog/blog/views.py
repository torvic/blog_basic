from django.shortcuts import render
from .models import post,categoria

# Create your views here.
def home(request):
    Post = post.objects.filter(estado=True)
    return render(request,'blog/index.html',context={'post':Post})

def generales(request):
    Categoria = categoria.objects.get(nombre='General')
    Post = post.objects.filter(
        estado=True, categoria=Categoria 
    )
    return render(request,'blog/generales.html',context={'post':Post})

def programacion(request):
    Categoria = categoria.objects.get(nombre='Programacion')
    Post = post.objects.filter(
        estado=True, categoria=Categoria 
    )
    return render(request,'blog/programacion.html',context={'post':Post})

def videojuegos(request):
    Categoria = categoria.objects.get(nombre='Videojuegos')
    Post = post.objects.filter(
        estado=True, categoria=Categoria 
    )
    return render(request,'blog/videojuegos.html',context={'post':Post})

def tutoriales(request):
    Categoria = categoria.objects.get(nombre='Tutoriales')
    Post = post.objects.filter(
        estado=True, categoria=Categoria 
    )
    return render(request,'blog/tutoriales.html',context={'post':Post})