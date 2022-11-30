from django.http import Http404
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from .models import TODO

# Create your views here.


def index(request):
    cases = TODO.objects.all().order_by('-id')
    return render(request, 'crud/index.html', {'todolist': cases, 'Title': 'TODO'})


def add(request):
    # прием запроса из формы
    title = request.POST['title']
    task = TODO(title=title)
    task.save()
    # перемещаемся на главную страницу
    return redirect('index')


def update(request, todoid):
    # ищем task по id
    task = TODO.objects.get(id=todoid)
    # меняем состояние
    task.taskcomplete = not task.taskcomplete
    task.save()
    return redirect('index')


def delete(request, todoid):
    task = TODO.objects.get(id=todoid)
    task.delete()
    return redirect('index')
