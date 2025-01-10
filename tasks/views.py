
from django.shortcuts import redirect, render, get_object_or_404
from django.utils import timezone
from django.contrib import messages
from .models import Task


def index(request):
    all_tasks = Task.objects.all()
    data = { "all_tasks": all_tasks}

    if request.method == 'GET':

        return render(request, 'tasks/index.html', data)
    
    elif request.method == 'POST':

        name = request.POST.get('name_task')

        task = Task()

        if not name.strip():
            return redirect('index')
        else:
            task.name_task = name
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
        
        name = request.POST.get('name_task')

        task = Task.objects.get(pk=id)
        
        if not name.strip():
            return render(request, 'tasks/update.html', {'task':task})
        else:
            task.name_task = name
            task.save()
        return render(request, 'tasks/detail.html', {'task':task})

def delete(request, id):

    task = get_object_or_404(Task,pk=id)
    task.delete()
    return redirect('index')