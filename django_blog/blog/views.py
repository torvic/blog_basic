from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'blog/index.html')

def generales(request):
    return render(request,'blog/generales.html')

def programacion(request):
    return render(request,'blog/programacion.html')

def videojuegos(request):
    return render(request,'blog/videojuegos.html')

def tutoriales(request):
    return render(request,'blog/tutoriales.html')