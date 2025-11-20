from django.shortcuts import render

# Create your views here.

from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from .models import Todo
from .forms import TodoForm


def index(request):
    """List todos and show a form to create a new todo."""
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse("todos:index"))
    else:
        form = TodoForm()

    todos = Todo.objects.all()
    return render(request, "todos/home.html", {"todos": todos, "form": form})


def edit_todo(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    if request.method == "POST":
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect(reverse("todos:index"))
    else:
        form = TodoForm(instance=todo)
    return render(request, "todos/edit.html", {"form": form, "todo": todo})


def toggle_complete(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    if request.method == "POST":
        if not todo.completed:
            todo.mark_completed()
        else:
            todo.mark_incomplete()
    return redirect(reverse("todos:index"))


def delete_todo(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    if request.method == "POST":
        todo.delete()
    return redirect(reverse("todos:index"))
