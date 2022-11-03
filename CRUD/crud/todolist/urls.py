from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add', views.add, name='add'),
    path('update/<int:todoid>', views.update, name='update'),
    path('delete/<int:todoid>', views.delete, name='delete')
]
