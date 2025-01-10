
from django.shortcuts import redirect, render, get_object_or_404
from django.utils import timezone
# from django.contrib import messages
from .forms import TaskCreateinForm
from .models import Task


def index(request):
    form = TaskCreateinForm()

    if request.method == 'GET':

        all_tasks = Task.objects.all().order_by('-created_date')
        return render(request, 'tasks/index.html', { "all_tasks": all_tasks, 'form':form})
    
    elif request.method == 'POST':

        form = TaskCreateinForm(request.POST)

        if form.is_valid():
            task = form.save(commit=False)
            task.created_date = timezone.now()
            task.save()
            return redirect('detail', id=task.task_id)
        else:
            return render(request, 'tasks/index.html', { "all_tasks": all_tasks, 'form':form})

def detail(request, id):
    try:
        task = get_object_or_404(Task,pk=id)
    except:
        return redirect("not_found")
    return render(request, 'tasks/detail.html', {'task':task})

def update(request, id):

    task = get_object_or_404(Task,pk=id)

    if request.method == 'GET':
        form = TaskCreateinForm(instance=task)
        return render(request, 'tasks/update.html', {'form': form, 'task':task})
    
    elif request.method == 'POST':
        
        form = TaskCreateinForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('detail',  id=task.task_id)
    else:
        form = TaskCreateinForm(instance=task)
    return render(request, 'tasks/update.html', {'form': form})

def delete(request, id):

    task = get_object_or_404(Task,pk=id)
    task.delete()
    return redirect('index')