from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def todo_list(request):
    return HttpResponse("투두 리스트")
    return render(request, "todo/list.html")
