from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm

def index(request):
    tasks = Task.objects.all().order_by('due_date')
    return render(request, 'todo/index.html', {'tasks': tasks})

def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = TaskForm()
    return render(request, 'todo/add_task.html', {'form': form})

def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    form = TaskForm(request.POST or None, instance=task)
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request, 'todo/edit_task.html', {'form': form})

def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect('index')

def complete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.completed = not task.completed
    task.save()
    return redirect('index')

