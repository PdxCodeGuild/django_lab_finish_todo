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
        'todo_types': todo_types
    }
    return render(request, 'todoapp/index.html', context)

# recieve a form submission to save a todo item
def save_todo(request):

    # get variables out of the form data
    todo_text = request.POST['todo_text']
    todo_type_ids = request.POST.getlist('todo_type_ids')

    # create an instance of the model and save it
    todo_item = TodoItem(text=todo_text)
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

def delete_todo(request, todo_id):
    # todo_item = get_object_or_404(TodoItem, pk=pk)
    todo_item = TodoItem.objects.get(id=todo_id)
    todo_item.delete()
    return HttpResponseRedirect(reverse('todoapp:index'))

def clear_all(request):
    todo_items = TodoItem.objects.all()
    todo_items.delete()

    return HttpResponseRedirect(reverse('todoapp:index'))
