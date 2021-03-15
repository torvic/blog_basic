from django.urls import path
from . import views


urlpatterns = [
    path('',views.home,name ='index'),
    path('generales/',views.generales,name ='generales'),
    path('programacion/',views.programacion,name ='programacion'),
    path('videojuegos/',views.videojuegos,name ='videojuegos'),
    path('tutoriales/',views.tutoriales,name ='tutoriales'),
    path('<slug:slug>/',views.detallePost,name ='detalle_post'),
]