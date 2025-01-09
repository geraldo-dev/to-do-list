from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Task


def index(request):

    all_tasks = Task.objects.all()
    data = {
        "all_tasks": all_tasks
    }
    return render(request, 'tasks/index.html', data)

def detail(request, id):
    # try:
    task = get_object_or_404(Task,pk=id)
    return render(request, 'tasks/detail.html', {'task':task})

def created(request, id):
    pass

def update(request, id):

    if request.method == 'GET':

        task = get_object_or_404(Task,pk=id)
        return render(request, 'tasks/update.html', {'task':task})
    
    elif request.method == 'POST':

        task = Task.objects.get(pk=id)
        print(task.name_task)
        task.name_task = request.POST.get('name_task')
        task.save()
        return render(request, 'tasks/detail.html', {'task':task})

def delete(request, id):
    pass