

from django.urls import path
from . import views
from django.conf.urls.static import static

app_name = 'todoapp'
urlpatterns = [
    path('index/', views.index, name='index'),
    path('new_todo/', views.new_todo, name='new_todo'),
    path('edit_todo/<int:todo_id>/', views.edit_todo, name='edit_todo'),
    path('update_todo/<int:todo_id>/', views.update_todo, name='update_todo'),
    path('save_todo/', views.save_todo, name='save_todo'),
    path('complete_todo/', views.complete_todo, name='complete_todo'),
    path('delete_todo/', views.delete_todo, name='delete_todo'),
    path('delete_all/', views.delete_all, name='delete_all'),
]


