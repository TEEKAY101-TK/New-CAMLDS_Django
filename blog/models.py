from django.db import models
from django.utils import timezone


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=60,unique=True)
    slug = models.CharField( max_length=100, unique=True)
     
    created_at = models.DateTimeField(auto_now_add=True) # set once at creation
    updated_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
    
class Tag(models.Model):
    name = models.CharField(max_length=30, unique=True)
    slug = models.SlugField(max_length=100, unique=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
  
class Post(models.Model):
    STATUS_CHOICES = (
         ("draft","Draft"),
         ("published","Published"),
     )   
    title =models.CharField(max_length=200)
    slug = models.SlugField(max_length=200,unique=True)
    body = models.TextField() 
    category = models.ForeignKey(Category, related_name="posts", on_delete=models.CASCADE) 
    published_at = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="draft")
    
    created_at = models.DateTimeField(auto_now_add=True) # set once at creation
    updated_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['published_at']
        
    def __str__(self):
        return self.name
