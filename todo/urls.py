from django.contrib import admin
from django.urls import path

from todo.views import todo_list

urlpatterns = [
    path("",todo_list) #127.0.0.1:8000/todo/list/
]
