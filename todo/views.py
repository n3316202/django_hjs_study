from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import generics,viewsets

from todo.models import Todo
from todo.serializers import TodoSerializer


# Create your views here.
def todo_list(request):
    #return HttpResponse("투두 리스트")
    return render(request, "todo/index.html")


class TodoGenericsListAPI(generics.ListAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

#delete update retrieve  3개를 담고 있음
#포스트 맨으로 method 를 위의 3개중 한개로 보내면 됨
class TodoRetrieveUpdateDestroyAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
