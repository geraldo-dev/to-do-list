from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Task


def index(request):

    all_tasks = Task.objects.all()
    data = {
        "all_tasks": all_tasks
    }
    return render(request, 'tasks/index.html', data)

def detail(request, id):
    try:
        task = Task.objects.get(pk=id)
    except Task.DoesNotExist:
        raise Http404('task não encontrada')
    return render(request, 'tasks/detail.html', {'task':task})

def created(request, id):
    pass

def update(request, id):
    pass

def delete(request, id):
    pass