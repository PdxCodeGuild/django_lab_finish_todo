from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.utils import timezone
from .models import TodoItem, TodoItemType
from django.contrib.auth.decorators import login_required

# index page, list todo items and a form
@login_required
def index(request):
    todo_items = request.user.todo_items.order_by('date_completed', 'date_created')
    context = {
        'todo_items': todo_items,
    }
    return render(request, 'todoapp/index.html', context)

@login_required
def new(request):
    todo_types = TodoItemType.objects.order_by('name')
    context = {
        'todo_types': todo_types
    }
    return render(request, 'todoapp/new.html', context)

@login_required
def edit(request, todo_item_id):
    todo_item = TodoItem.objects.get(id=todo_item_id)
    if todo_item.user.id != request.user.id:
        raise Http404
        # return HttpResponseRedirect(reverse('users:login_register'))
    todo_types = TodoItemType.objects.order_by('name')
    context = {
        'todo_item': todo_item,
        'todo_types': todo_types
    }
    return render(request, 'todoapp/edit.html', context)

@login_required
def save_edit(request):
    # get variables out of the form data
    todo_id = request.POST['todo_id']
    todo_text = request.POST['todo_text']
    todo_type_ids = request.POST.getlist('todo_type_ids')
    todo_extra_text = request.POST['todo_extra_text']
    
    todo_item = TodoItem.objects.get(id=todo_id)
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


# recieve a form submission to save a todo item
@login_required
def save_todo(request):
    
    # get variables out of the form data
    todo_text = request.POST['todo_text']
    todo_type_ids = request.POST.getlist('todo_type_ids')
    todo_extra_text = request.POST['todo_extra_text']
    
    # create an instance of the model and save it
    todo_item = TodoItem(text=todo_text, extra_text=todo_extra_text, user=request.user)
    todo_item.save()
    
    # create many-to-many relationship with types
    for todo_type_id in todo_type_ids:
        todo_type = TodoItemType.objects.get(id=todo_type_id)
        todo_item.types.add(todo_type)
    
    # redirect to the index page
    return HttpResponseRedirect(reverse('todoapp:index'))

# receieve a form submission to complete a todo item
@login_required
def complete_todo(request):
    todo_item_id = request.POST['todo_item_id']
    todo_item = TodoItem.objects.get(id=todo_item_id)
    todo_item.date_completed = timezone.now()
    todo_item.save()
    return HttpResponseRedirect(reverse('todoapp:index'))

@login_required
def clear_todo(request, todo_item_id):
    todo_item = TodoItem.objects.get(id=todo_item_id)
    todo_item.delete()
    return HttpResponseRedirect(reverse('todoapp:index'))

@login_required
def clear_tags(request):
    todo_item_id = request.GET['todo_item_id']
    todo_item = TodoItem.objects.get(id=todo_item_id)
    todo_item.types.clear()
    return HttpResponseRedirect(reverse('todoapp:index'))

@login_required
def clear_all(request):
    todo_items = TodoItem.objects.filter(date_completed__isnull=False)
    todo_items.delete()
    
    # todo_items = TodoItem.objects.all()
    # for todo_item in todo_items:
    #     if todo_item.date_completed is not None:
    #         todo_item.delete()
    
    return HttpResponseRedirect(reverse('todoapp:index'))
    