from django.shortcuts import render
from .models import post,categoria
from django.shortcuts import get_object_or_404
from django.db.models import Q
from django.core.paginator import Paginator

def home(request):
    # Filtramos todos los post, en la cual todos sus estados sean Publicados (True).
    Post = post.objects.filter(estado=True)
    # Extraemos del index.html la cadena almacenada en 'buscar'
    queryset = request.GET.get('buscar')

    if queryset:
        # Filtro los post de acuerdo al queryset
        Post = post.objects.filter(
            Q(titulo__icontains = queryset) |
            Q(descripcion__icontains = queryset)
        ).distinct()
    
    # retornamos el index.html con los post filtrados.
    return render(request,'blog/index.html', context={'post':Post})

def detallePost(request,slug):
    #Post = post.objects.get(slug = slug)
    #print(Post)
    Post = get_object_or_404(post,slug=slug)
    return render(request,'blog/post.html',context={'detalle_post':Post})

def generales(request):
    # Filtrar Post solo generales.
    Post = post.objects.filter(
        estado=True, 
        categoria=categoria.objects.get(nombre__iexact='General')
    )
    # Extraer la cadena de 'buscar'.
    queryset = request.GET.get('buscar')

    if queryset:
        # Filtrar Post solo generales y de acuerdo al queryset.
        Post = post.objects.filter(
            Q(titulo__icontains = queryset) |
            Q(descripcion__icontains = queryset),
            estado=True, 
            categoria=categoria.objects.get(nombre__iexact='General')
    ).distinct()

    return render(request,'blog/generales.html',context={'post':Post})

def programacion(request):
    # Filtrar Post solo programacion.
    Post = post.objects.filter(
        estado=True, 
        categoria=categoria.objects.get(nombre__iexact='programacion')
    )
    # Extraer la cadena de 'buscar'.
    queryset = request.GET.get('buscar')

    if queryset:
        # Filtrar Post solo programacion y de acuerdo al queryset.
        Post = post.objects.filter(
            Q(titulo__icontains = queryset) |
            Q(descripcion__icontains = queryset),
            estado=True, 
            categoria=categoria.objects.get(nombre__iexact='programacion')
    ).distinct()

    return render(request,'blog/programacion.html',context={'post':Post})

def videojuegos(request):
    # Filtrar Post solo videojuegos.
    Post = post.objects.filter(
        estado=True, 
        categoria=categoria.objects.get(nombre__iexact='videojuegos')
    )
    # Extraer la cadena de 'buscar'.
    queryset = request.GET.get('buscar')

    if queryset:
        # Filtrar Post solo videojuegos y de acuerdo al queryset.
        Post = post.objects.filter(
            Q(titulo__icontains = queryset) |
            Q(descripcion__icontains = queryset),
            estado=True, 
            categoria=categoria.objects.get(nombre__iexact='videojuegos')
    ).distinct()

    return render(request,'blog/videojuegos.html',context={'post':Post})

def tutoriales(request):
    # Filtrar Post solo tutoriales.
    Post = post.objects.filter(
        estado=True, 
        categoria=categoria.objects.get(nombre__iexact='tutoriales')
    )
    # Extraer la cadena de 'buscar'.
    queryset = request.GET.get('buscar')

    if queryset:
        # Filtrar Post solo tutoriales y de acuerdo al queryset.
        Post = post.objects.filter(
            Q(titulo__icontains = queryset) |
            Q(descripcion__icontains = queryset),
            estado=True, 
            categoria=categoria.objects.get(nombre__iexact='tutoriales')
    ).distinct()

    return render(request,'blog/tutoriales.html',context={'post':Post})