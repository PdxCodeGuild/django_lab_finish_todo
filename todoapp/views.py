from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone
from .models import TodoItem, TodoItemType

# index page, list todo items and a form
def index(request):
    todo_items = TodoItem.objects.order_by('date_completed', 'date_created')
    todo_types = TodoItemType.objects.order_by('name')
    
    context = {
        'todo_items': todo_items,
        'todo_types': todo_types, 
    }
    return render(request, 'todoapp/index.html', context)

# recieve a form submission to save a todo item
def save_todo(request):
    
    # get variables out of the form data
    todo_text = request.POST['todo_text']
    todo_type_ids = request.POST.getlist('todo_type_ids')
    todo_extra_text = request.POST['todo_extra_text']
    
    # create an instance of the model and save it
    todo_item = TodoItem(text=todo_text, extra_text=todo_extra_text)
    todo_item.save()

    
    # create many-to-many relationship with types
    for todo_type_id in todo_type_ids:
        todo_type = TodoItemType.objects.get(id=todo_type_id)
        todo_item.types.add(todo_type)
    
    # redirect to the index page
    return HttpResponseRedirect(reverse('todoapp:index'))

# receieve a form submission to complete a todo item
def complete_todo(request):
    todo_item_id = request.POST['todo_item_id']
    todo_item = TodoItem.objects.get(id=todo_item_id)
    todo_item.date_completed = timezone.now()
    todo_item.save()
    return HttpResponseRedirect(reverse('todoapp:index'))


def delete_todo(request):
    todo_item_delete = request.POST['todo_item_delete']
    todo_item = TodoItem.objects.get(id=todo_item_delete)
    todo_item.delete()
    return HttpResponseRedirect(reverse('todoapp:index'))
    

def delete_all(request):
    todo_item_delete_all = request.POST['todo_item_delete_all']
    todo_item = TodoItem.objects.all()
    todo_item.delete()
    return HttpResponseRedirect(reverse('todoapp:index'))
    

def new_todo(request):
    todo_types = TodoItemType.objects.order_by('name')
    
    context = {
        'todo_types': todo_types, 
    }
    return render(request, 'todoapp/new_todo.html', context)
    

def edit_todo(request, todo_id):
    todo_item = TodoItem.objects.get(id=todo_id)
    
    todo_types = TodoItemType.objects.order_by('name')
    
    context = {
        "todo_item": todo_item,
        "todo_types": todo_types,
    }
    
    return render(request, 'todoapp/edit_todo.html', context)


def update_todo(request, todo_id):
    
    todo_item = TodoItem.objects.get(id=todo_id)
    
    # get variables out of the form data
    todo_text = request.POST['todo_text']
    todo_type_ids = request.POST.getlist('todo_type_ids')
    todo_extra_text = request.POST['todo_extra_text']
    print(todo_text)
    print(todo_extra_text)
    
    todo_item.text = todo_text
    todo_item.extra_text = todo_extra_text
    todo_item.save()

    
    todo_item.types.clear()
    
    # create many-to-many relationship with types
    for todo_type_id in todo_type_ids:
        todo_type = TodoItemType.objects.get(id=todo_type_id)
        todo_item.types.add(todo_type)
        
    
    # redirect to the index page
    return HttpResponseRedirect(reverse('todoapp:index'))
    
