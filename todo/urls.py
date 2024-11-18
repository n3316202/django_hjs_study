from django.contrib import admin
from django.urls import include, path

from todo.views import TodoGenericsListAPI, TodoRetrieveUpdateDestroyAPI, TodoViewSet, todo_list
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("",TodoViewSet)

urlpatterns = [
    path("",todo_list), #127.0.0.1:8000/todo/list/    
    path("generics/list", TodoGenericsListAPI.as_view(), name=""),
    path("generics/<int:pk>", TodoRetrieveUpdateDestroyAPI.as_view(), name=""),
    path("viewsets/",include(router.urls)),
]
