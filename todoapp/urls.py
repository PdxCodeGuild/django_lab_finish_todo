

from django.urls import path
from . import views

app_name = 'todoapp'
urlpatterns = [
    path('index/', views.index, name='index'),
    path('save_todo/', views.save_todo, name='save_todo'),
    path('complete_todo/', views.complete_todo, name='complete_todo'),
    path('delete_todo/<int:todo_id>/', views.delete_todo, name='delete_todo'),
]
