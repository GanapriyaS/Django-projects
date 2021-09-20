from django.db import models

# Create your models here.
class Todo(models.Model):
    title=models.CharField(max_length=255)
    desc=models.TextField()
    num=models.IntegerField()
    create=models.DateTimeField(auto_now_add=True)
