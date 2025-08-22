from django.contrib import admin


# Register your models here.

from .models import Category, Post, Tag

admin.site.register(Category)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    #list view
    list_display = ("title","category","status","published_at","created_at",)
    list_filter = ("status","category")
    search_fields = ("title","body")
    date_hierarchy = "published_at"
    ordering = ("-published_at",)
    
prepopulated_fields = {"slug": ("title,")}
readonly_fields = ("created_at", "updated_at")
fieldsets = (
    ("Basic info", {
        "fields": ("title", "slug", "status"),
    }),
    )
("content",({
        "fields": ("body",),
    }),
    )
("Relationships & Dates", ({
        "fields": ("category", "published_at"),
    }),
    )
("Timestamps",({
        "fields": ("created_at", "updated_at"),
    }),
    )


    
admin.site.register(Tag)




# python manage.py makemigrations
# python manage.py migrate
# python manage.py runserver
# python manage.py createsuperuser
