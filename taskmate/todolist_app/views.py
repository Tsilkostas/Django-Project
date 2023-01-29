from django.shortcuts import render
from django.http  import HttpResponse

def todolist(request):
    return HttpResponse("Welcome To Task Page")
