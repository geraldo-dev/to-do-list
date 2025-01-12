
from django.shortcuts import redirect, render, get_object_or_404
from django.utils import timezone
from .forms import TaskCreateinForm, TaskUpdateForm
from django.core.paginator import Paginator
from .models import Task


def index(request):
    form = TaskCreateinForm()

    if request.method == 'GET':

        list_tasks = Task.objects.all().order_by('-is_activer','-created_date')

        paginator = Paginator(list_tasks, 5)
        page = request.GET.get('page')

        all_tasks = paginator.get_page(page)
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
        return redirect("index")
    return render(request, 'tasks/detail.html', {'task':task})

def update(request, id):

    task = get_object_or_404(Task,pk=id)

    if request.method == 'GET':
        form = TaskUpdateForm(instance=task)
        return render(request, 'tasks/update.html', {'form': form, 'task':task})
    
    elif request.method == 'POST':
        
        form = TaskUpdateForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('detail',  id=task.task_id)
    else:
        form = TaskUpdateForm(instance=task)
    return render(request, 'tasks/update.html', {'form': form})

def delete(request, id):

    task = get_object_or_404(Task,pk=id)
    task.delete()
    return redirect('index')

def activer(request, id):
    task = Task.objects.get(pk=id)

    if request.method == 'GET':
        print(task.is_activer)
        if task.is_activer == True:
            task.is_activer = False
        else:
            task.is_activer = True
        task.save()
        return redirect('index')