from django.shortcuts import render, redirect, get_object_or_404
from .models import ToDoItem

def home(request):
    if request.method == 'POST':
        task = request.POST.get('task')
        if task:
            ToDoItem.objects.create(description=task)
        return redirect('home')

    tasks = ToDoItem.objects.all()
    return render(request, "home.html", {"tasks": tasks})

def delete_task(request, task_id):
    if request.method == "POST":
        task = get_object_or_404(ToDoItem, id=task_id)
        task.delete()
    return redirect("home")

def open_task(request, task_id):
    if request.method == "POST":
        task = get_object_or_404(ToDoItem, id=task_id)
        task.completed = True
        task.save()
    return redirect("home")

def close_task(request, task_id):
    if request.method == "POST":
        task = get_object_or_404(ToDoItem, id=task_id)
        task.completed = False
        task.save()
    return redirect("home")
