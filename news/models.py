from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name_plural = 'News Category'

class News (models.Model):
    title = models.CharField(max_length=255)
    image = models.FileField(upload_to='news')    
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    posted_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    views_count = models.PositiveIntegerField(default=0)
    is_editorial = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name_plural = 'News'

        
