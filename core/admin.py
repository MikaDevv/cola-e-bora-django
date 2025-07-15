from django.contrib import admin

# Register your models here.

from .models import PerfilUsuario, Categoria, Tarefa

admin.site.register(PerfilUsuario)
admin.site.register(Categoria)
admin.site.register(Tarefa)