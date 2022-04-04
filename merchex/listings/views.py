from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    return HttpResponse('<h1>Premier test</h1>')


def aboutus(request):
    return HttpResponse('<h1>Deuxième test</h1>')