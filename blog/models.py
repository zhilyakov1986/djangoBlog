from django.db import models
from datetime import datetime

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    created_at = models.DateTimeField(default=datetime.now, blank = True )   
    class Meta:
        verbose_name_plural = "Blogs"
    def __str__(self):
        return self.title