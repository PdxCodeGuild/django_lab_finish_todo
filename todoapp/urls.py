

from django.urls import path
from . import views

app_name = 'todoapp'
urlpatterns = [
    path('index/', views.index, name='index'),
    path('save_todo/', views.save_todo, name='save_todo'),
    path('complete_todo/', views.complete_todo, name='complete_todo'),
    path('clear_todo/', views.clear_todo, name='clear_todo'),
    path('clear_all/', views.clear_all, name='clear_all'),
    path('save/', views.save_page, name='save_page'),
    path('edit/<int:todo_item_id>/', views.edit_page, name='edit_page'),
    path('edit_todo/', views.edit_todo, name='edit_todo')
]


