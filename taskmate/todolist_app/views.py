from django.shortcuts import render
from django.http  import HttpResponse
from todolist_app.models import TaskList

def todolist(request):
    all_tasks = TaskList.objects.all
    
    return render(request, 'todolist.html',{'all_tasks':all_tasks})

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