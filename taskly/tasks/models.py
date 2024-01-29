from django.db import models
from users.models import User

# Create your models here.
class Task(models.Model):
    uuid = models.CharField('uuid', null= False, blank = False, max_length = 40)
    title = models.TextField('title', blank = False, null = False, max_length = 50)
    description = models.CharField('description', blank = True, max_length = 200)
    date = models.TextField('date', blank = False, null = False, max_length = 100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.title