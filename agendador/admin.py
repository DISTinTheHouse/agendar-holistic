from django.contrib import admin
from .models import Cita

@admin.register(Cita)
class CitaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'correo', 'fecha', 'hora', 'confirmado', 'creado_en')
    list_filter = ('fecha', 'confirmado')
    search_fields = ('nombre', 'correo', 'direccion')
