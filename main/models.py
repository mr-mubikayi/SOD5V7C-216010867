from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.CharField(max_length=100)
    publication_date = models.DateField()
    views = models.IntegerField(default=0)
    
    def __str__(self):
        return self.title
