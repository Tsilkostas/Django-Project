
from django.urls import path
from todolist_app import views

urlpatterns = [
    path('', views.todolist, name='todolist'),
    path('delete/<task_id>', views.delete_task, name='delete_task'),
    path('contact', views.contact, name='contact'),
    path('about', views.about, name='about'),
]