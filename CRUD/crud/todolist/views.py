from django.shortcuts import render, redirect
from .models import TODO
from django.views.decorators.http import require_http_methods

# Create your views here.


def index(request):
    cases = TODO.objects.all()
    return render(request, 'crud/index.html', {'todolist': cases, 'Title': 'Main page'})


@require_http_methods(['POST'])
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
    # указываем, что task не выполнен
    task.taskcomplete = not task.taskcomplete
    task.save()
    return redirect('index')


def delete(request, todoid):
    task = TODO.objects.get(id=todoid)
    task.delete()
    return redirect('index')
