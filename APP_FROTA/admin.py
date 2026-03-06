from django.contrib import admin
from .models import Veiculo

@admin.register(Veiculo)
class VeiculoAdmin(admin.ModelAdmin):
    list_display = ('placa', 'modelo', 'tipo_frota', 'condutor', 'seguradora')
    search_fields = ('placa', 'modelo', 'condutor')
    list_filter = ('tipo_frota', 'seguradora')
