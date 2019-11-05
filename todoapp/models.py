from django.db import models
from django.contrib.auth.models import User

class TodoItemType(models.Model):
    name = models.CharField(max_length=200)
    emoji = models.CharField(max_length=5)
    
    def __str__(self):
        return self.emoji + ' ' + self.name


class TodoItem(models.Model):
    text = models.CharField(max_length=500)
    date_created = models.DateTimeField(auto_now_add=True)
    date_completed = models.DateTimeField(null=True, blank=True)
    extra_text = models.TextField()
    types = models.ManyToManyField(TodoItemType)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='todo_items')
    
    def ordered_types(self):
        return self.types.order_by('name')
    
    def __str__(self):
        return self.user.username + ' ' + self.text


