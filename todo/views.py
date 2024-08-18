from django.shortcuts import render
from .models import ToDo
# Create your views here.


def todo_list(request):
    return render(request, 'todo/todo_list.html', {})
