from django.shortcuts import render, redirect, get_object_or_404
from django.core.handlers.wsgi import WSGIRequest
from webapp.models import Task, StatusChoice
from webapp.forms import TaskForm


def add_view(request: WSGIRequest):
    if request.method == "GET":
        form = TaskForm()
        return render(request, 'task_create.html',
                      context={
                          'choices': StatusChoice.choices,
                          'form': form
                        })

    form = TaskForm(data=request.POST)

    if not form.is_valid():
        return render(request, 'task_create.html',
                      context={
                          'choices': StatusChoice.choices,
                          'form': form
                      })
    else:
        task = Task.objects.create(**form.cleaned_data)
        return redirect('task_detail', pk=task.pk)


def detail_view(request, pk):
    task = get_object_or_404(Task, pk=pk)
    context = {'task': task}
    return render(request, 'task.html', context=context)


def update_view(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_detail', pk=task.pk)
        return render(request, 'task_update.html', context={'form': form, 'task': task})

    form = TaskForm(instance=task)
    return render(request, 'task_update.html', context={'form': form, 'task': task})


def delete_view(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'task_confirm_delete.html', context={'task': task})


def confirm_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('index')






