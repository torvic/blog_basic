# Generated by Django 2.2.1 on 2021-03-13 03:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='autor',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombres', models.CharField(max_length=255, verbose_name='Nombres de autor')),
                ('apellidos', models.CharField(max_length=255, verbose_name='Apellidos de autor')),
                ('facebook', models.URLField(blank=True, null=True, verbose_name='Facebook')),
                ('twitter', models.URLField(blank=True, null=True, verbose_name='Twitter')),
                ('instagram', models.URLField(blank=True, null=True, verbose_name='Instagram')),
                ('web', models.URLField(blank=True, null=True, verbose_name='Web')),
                ('correo', models.EmailField(max_length=254, verbose_name='Correo Electronico')),
                ('estado', models.BooleanField(default=True, verbose_name='Autor Activo/No Activo')),
                ('fecha_creacion', models.DateField(auto_now_add=True, verbose_name='Fecha de Creacion')),
            ],
            options={
                'verbose_name': 'autor',
                'verbose_name_plural': 'autores',
            },
        ),
        migrations.CreateModel(
            name='categoria',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre de la categoria')),
                ('estado', models.BooleanField(default=True, verbose_name='Categoria Activada/Categoria no Activada')),
                ('fecha_creacion', models.DateField(auto_now_add=True, verbose_name='Fecha de creacion')),
            ],
            options={
                'verbose_name': 'categoria',
                'verbose_name_plural': 'categorias',
            },
        ),
    ]