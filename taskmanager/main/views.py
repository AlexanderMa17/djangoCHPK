from django.shortcuts import render, redirect
from django.template import RequestContext
from django.urls import reverse
from django.utils.safestring import mark_safe

from .forms import TaskForm
from .models import Task


def index(request):
    tasks = Task.objects.order_by('-id')[:5]
    return render(request, 'main/index.html', {'title': 'Главная страница сайта', 'tasks': tasks})


def about(request):
    return render(request, 'main/about.html')


def create(request):
    form = TaskForm()
    context = {
        'form': form
    }
    return render(request, 'main/create.html')





