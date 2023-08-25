from django.contrib import admin
from .models import Cliente, Endereco

#admin.site.register(Cliente)
#admin.site.register(Endereco)

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'cpf', 'telefone', 'email')
    list_filter = ('cpf', 'nome')
    list_display_links = ('nome',)
    search_fields = ('id',)

@admin.register(Endereco)
class EnderecoAdmin(admin.ModelAdmin):
    list_display = ('logradouro', 'numero', 'bairro', 'cidade', 'estado', 'cep')
    search_fields = ('logradouro', 'cidade', 'estado', 'cep')