from django.shortcuts import render, HttpResponse

# Create your views here.

def hello(request, nome, idade):
    return HttpResponse('<h1>Hello {} de {} anos</h1>'.format(nome, idade))

def helloMundo(requet):
    return HttpResponse('<h1> Olá Mumdo</h1>')

def soma(request, n1, n2):
    adicao = n1 + n2
    return HttpResponse('<h1>A soma de {} + {} é : {}</h1>'.format(n1,n2,adicao))