from django.shortcuts import render
from .models import Transacao
from .form import TransacaoForm
# Create your views here.

def home(request):

    dados = {}
    dados['transacoes'] = Transacao.objects.all()
    return render(request, 'despesa/home.html', dados)

def criar (request):
    form = TransacaoForm(request.POST or None)
    dados = {}
    if form.is_valid():
        form.save()
        return home(request)
    dados['form'] = form
    return render(request, 'despesa/form.html', dados)

def update(request, pk):
    transacao = Transacao.objects.get(pk=pk)
    form = TransacaoForm(request.POST or None, instance=transacao)
    dados = {}
    if form.is_valid():
        form.save()
        return home(request)
    dados['form'] = form
    return render(request, 'despesa/form.html', dados)

def delete(request, pk):
    transacao = Transacao.objects.get(pk=pk)
    transacao.delete()
    return home(request)
