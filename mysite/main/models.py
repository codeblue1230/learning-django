from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ToDoList(models.Model): # Cascade deletes all children attached to this model
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="todolist", null=True) 
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    

class Item(models.Model):
    todolist = models.ForeignKey(ToDoList, on_delete=models.CASCADE)
    text = models.CharField(max_length=300)
    complete = models.BooleanField()

    def __str__(self):
        return self.text
    
# Remember to make changes to database with python manage.py makemigrations, then run python manage.py migrate
# If this doesn't work delete everything in each migrations folder except __init__ files
# and delete your db.sqlite, and all __pycache__ folders as well