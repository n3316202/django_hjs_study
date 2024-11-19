from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import generics,viewsets

from todo.models import Todo
from todo.serializers import TodoSerializer

from rest_framework.permissions import IsAuthenticated

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


#함수에서는 @permission_classes 데코레이터 형식으로 호출
# from rest_framework.decorators import permission_classes
# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
# def example_view(request, format=None)
#     content = {'status' : 'request was permitted'}
#     returnn Response(content)

class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all().order_by("-created_at") #앞에 - 내림차순 없으면 오름차순
    serializer_class = TodoSerializer
    permission_classes = [IsAuthenticated] # 로그인 된 유저만 해당 View 를 호출 할수 있음
