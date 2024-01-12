from django.http import HttpResponse
from django.shortcuts import redirect, render

from .models import Task

def addTask(request):
    if request.POST['task']:
        task = request.POST['task']
        Task.objects.create(task=task)
    else:
        print('No task found')

    return redirect('home')