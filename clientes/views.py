from django.shortcuts import render
from django.http import HttpResponse
from .models import Cliente, Carro

def clientes(request):
    if request.method == "GET":
        return render(request, 'clientes.html')
    elif request.method == "POST":
        nome = request.POST.get('nome')
        sobrenome = request.POST.get('sobrenome')
        email = request.POST.get('email')
        cpf = request.POST.get('cpf')
        carro = request.POST.getlist('carro')
        placas = request.POST.getlist('placa')
        ano = request.POST.getlist('ano')

        cliente = Cliente(
            nome = nome,
            sobrenome = sobrenome,
            email = email,
            cpf = cpf
        )
        
        cliente.save()

        
        return HttpResponse('teste')        
