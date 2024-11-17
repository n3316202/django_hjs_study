from django.contrib import admin
from django.urls import path

from todo.views import TodoGenericsListAPI, TodoRetrieveUpdateDestroyAPI, todo_list

urlpatterns = [
    path("",todo_list), #127.0.0.1:8000/todo/list/
    path("generics/list", TodoGenericsListAPI.as_view(), name=""),
    path("generics/<int:pk>", TodoRetrieveUpdateDestroyAPI.as_view(), name=""),
]
