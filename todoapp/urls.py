

from django.urls import path
from . import views

app_name = 'todoapp'
urlpatterns = [
    path('index/', views.index, name='index'),
    path('save_todo/', views.save_todo, name='save_todo'),
    path('complete_todo/', views.complete_todo, name='complete_todo'),
    path('clear_todo/<int:todo_item_id>/', views.clear_todo, name='clear_todo'),
    path('clear_tags/', views.clear_tags, name='clear_tags'),
    path('clear_all/', views.clear_all, name='clear_all'),
    path('new/', views.new, name='new'),
    path('edit/<int:todo_item_id>/', views.edit, name='edit'),
    path('save_edit/', views.save_edit, name='save_edit')
]


