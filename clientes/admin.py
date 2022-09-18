from django.contrib import admin
from .models import Carro, Cliente


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = [
        'nome', 'sobrenome', 'email', 'cpf'
    ]


@admin.register(Carro)
class CarroAdmin(admin.ModelAdmin):
    list_display = [
        'carro', 'placa', 'ano', 'cliente', 'lavagens', 'consertos'
    ]
