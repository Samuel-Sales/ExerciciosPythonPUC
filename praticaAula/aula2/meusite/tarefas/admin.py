from django.contrib.admin import site
from tarefas.models import Tarefa
from django.contrib.admin import ModelAdmin

# Register your models here.
class TarefaAdmin(ModelAdmin):
    fields = ['nome', 'descricao', 'status']

site.register(Tarefa, TarefaAdmin)
# site.register(Tarefa)