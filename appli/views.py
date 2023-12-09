from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def example(request):
    return HttpResponse('This is the example for Django')