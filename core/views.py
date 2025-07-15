from django.shortcuts import render, redirect
from .models import Tarefa, Categoria
from .forms import TarefaForm
from django.contrib.auth.decorators import login_required

def home(request):
    tarefas_abertas = Tarefa.objects.filter(estado='ABERTA').order_by('-data_criacao')
    context = {
        'tarefas': tarefas_abertas
    }
    return render(request, 'core/home.html', context)

@login_required
def criar_tarefa(request):
    if request.method == 'POST':
        form = TarefaForm(request.POST)
        if form.is_valid():
            tarefa = form.save(commit=False)
            tarefa.criador = request.user
            tarefa.save()
            return redirect('home')
    else:
        form = TarefaForm()

    context = {
        'form': form
    }
    return render(request, 'core/criar_tarefa.html', context)