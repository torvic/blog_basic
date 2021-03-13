from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class categoria(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField('Nombre de la categoria',max_length=100,null=False,blank=False)
    estado = models.BooleanField('Categoria Activada/Categoria no Activada',default=True)
    fecha_creacion = models.DateField('Fecha de creacion',auto_now=False,auto_now_add=True)
    
    class Meta:
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'
        
    def __str__(self):
        return self.nombre
    
class autor(models.Model):
    id = models.AutoField(primary_key=True)
    nombres = models.CharField('Nombres de autor',max_length=255,null=False,blank=False)
    apellidos = models.CharField('Apellidos de autor',max_length=255,null=False,blank=False)
    facebook = models.URLField('Facebook',null=True,blank=True)
    twitter = models.URLField('Twitter',null=True,blank=True)
    instagram = models.URLField('Instagram',null=True,blank=True)
    web = models.URLField('Web',null=True,blank=True)
    correo = models.EmailField('Correo Electronico',null=False,blank=False)
    estado = models.BooleanField('Autor Activo/No Activo',default=True)
    fecha_creacion = models.DateField('Fecha de Creacion',auto_now=False,auto_now_add=True)
    
    class Meta:
        verbose_name = 'autor'
        verbose_name_plural = 'autores'
        
    def __str__(self):
        return "{0},{1}".format(self.apellidos, self.nombres)

class post(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField('Titulo',max_length=90,blank=False,null=False)
    slug = models.CharField('Slug',max_length=100,blank=False,null=False)
    descripcion = models.CharField('Descripcion',max_length=110,blank=False,null=False)
    contenido = RichTextField('Contenido')
    imagen = models.URLField(max_length=255,blank=False,null=False)
    autor = models.ForeignKey(autor, on_delete=models.CASCADE)
    categoria = models.ForeignKey(categoria,on_delete=models.CASCADE)
    estado = models.BooleanField('Publicado/No publicado',default=True)
    fecha_creacion = models.DateField('Fecha de creacion',auto_now=False,auto_now_add=True)
    
    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'
        
    def __str__(self):
        return self.titulo
    