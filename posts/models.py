from django.db import models

# Create your models here.

class Posts(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    
    def __str__(self):
        return str(self.title)