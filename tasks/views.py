from django.shortcuts import redirect, render, get_object_or_404
from django.utils import timezone
from .models import Task


def index(request):
    all_tasks = Task.objects.all()
    data = { "all_tasks": all_tasks}

    if request.method == 'GET':

        return render(request, 'tasks/index.html', data)
    
    elif request.method == 'POST':

        task = Task()
        task.name_task = request.POST.get('name_task')
        task.created_date = timezone.now()
        task.save()
        return redirect('index')

def detail(request, id):
    try:
        task = get_object_or_404(Task,pk=id)
    except:
        return redirect("index")
    return render(request, 'tasks/detail.html', {'task':task})

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

    task = get_object_or_404(Task,pk=id)
    task.delete()
    return redirect('index')