from django.contrib import admin
from .models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin

class categoriaResource(resources.ModelResource):
    class Meta:
        model = categoria
        
# Register your models here.
class categoriaAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['nombre']
    list_display = ('nombre','estado','fecha_creacion')
    resources_class = categoriaResource

class autorResource(resources.ModelResource):
    class Meta:
        model = autor
    
class autorAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['nombres','apellidos','correo']
    list_display = ('nombres','apellidos','correo','estado','fecha_creacion')
    resources_class = autorResource


admin.site.register(categoria, categoriaAdmin)
admin.site.register(autor, autorAdmin)
admin.site.register(post)