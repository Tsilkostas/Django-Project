from django.shortcuts import render
from django.http  import HttpResponse

def todolist(request):
    context={
        'welcome_text':'Welcome to To Do List page'
        
    }
    return render(request, 'todolist.html',context)

def contact(request):
    context={
        'contact_text':'Welcome to Contact page'
        
    }
    return render(request, 'contact.html',context)

def about(request):
    context={
        'about_text':'Welcome to About page'
        
    }
    return render(request, 'about.html',context)