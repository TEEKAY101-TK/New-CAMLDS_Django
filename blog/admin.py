from django.contrib import admin
from django.urls import path

# Register your models here.

from .models import Category, Post

admin.site.register(Category)
admin.site.register(Post)
# python manage.py makemigrations
# python manage.py migrate
# python manage.py runserver
# python manage.py createsuperuser
