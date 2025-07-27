from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def home(request):
    context = {
        'name': 'Girish',
        'framework': 'Django',
        'year': 2025
    }
    return render(request, 'home.html', context)

