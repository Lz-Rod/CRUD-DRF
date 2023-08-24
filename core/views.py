from django.shortcuts import render, redirect
from .models import Cliente

def home(request):
    vcliente = Cliente.objects.all()
    return render(request, "index.html", {"vcliente": vcliente})

def save(request):
    vnome = request.POST.get("nome")
    Cliente.objects.create(nome=vnome)
    vcliente = Cliente.objects.all()
    return render(request, "index.html", {"vcliente": vcliente})

def edit(request, id):
    vcliente = Cliente.objects.get(id=id)
    return render(request, "update.html", {"vcliente": vcliente})

def update(request, id):
    vnome = request.POST.get("nome")
    vcliente = Cliente.objects.get(id=id)
    vcliente.nome = vnome
    vcliente.save()
    return redirect(home)

def delete(request, id):
    vcliente = Cliente.objects.get(id=id)
    vcliente.delete()
    return redirect(home)