from django.contrib import admin


# Register your models here.

from .models import Category, Post

admin.site.register(Category)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    #list view
    list_display = ("title","category","status","published_at","created_at",)
    list_filter = ("status","category")
    search_fields = ("title","body")
    date_hierarchy = "published_at"
    ordering = ("-published_at",)

# python manage.py makemigrations
# python manage.py migrate
# python manage.py runserver
# python manage.py createsuperuser
