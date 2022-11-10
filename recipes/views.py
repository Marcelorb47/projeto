from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'recipes/pages/home.html', context={
        'name': 'Marcelo Rodrigues'
    })


def contato(request):
    return HttpResponse('Contato')


def sobre(request):
    return HttpResponse('sobre')
