from django.shortcuts import render
from .models import post,categoria
from django.shortcuts import get_object_or_404

# Create your views here.
def home(request):
    Post = post.objects.filter(estado=True)
    return render(request,'blog/index.html',context={'post':Post})

def detallePost(request,slug):
    #Post = post.objects.get(slug = slug)
    #print(Post)
    Post = get_object_or_404(post,slug=slug)
    return render(request,'blog/post.html',context={'detalle_post':Post})

def generales(request):
    Categoria = categoria.objects.get(nombre__iexact='General')
    Post = post.objects.filter(
        estado=True, categoria=Categoria 
    )
    print('este es: ',Post)
    return render(request,'blog/generales.html',context={'post':Post})

def programacion(request):
    Categoria = categoria.objects.get(nombre__iexact='Programacion')
    Post = post.objects.filter(
        estado=True, categoria=Categoria 
    )
    return render(request,'blog/programacion.html',context={'post':Post})

def videojuegos(request):
    Categoria = categoria.objects.get(nombre__iexact='Videojuegos')
    Post = post.objects.filter(
        estado=True, categoria=Categoria 
    )
    return render(request,'blog/videojuegos.html',context={'post':Post})

def tutoriales(request):
    Categoria = categoria.objects.get(nombre__iexact='Tutoriales')
    Post = post.objects.filter(
        estado=True, categoria=Categoria 
    )
    return render(request,'blog/tutoriales.html',context={'post':Post})