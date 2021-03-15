from django.contrib import admin
from .models import deportes,articulo,comentarios

models = deportes,articulo,comentarios
admin.site.register(models)
