

from django.contrib import admin
from django.utils import timezone
from.models import Category, Post, Tag


class PostTagInline(admin.TabularInline):
    model = Post.tags.through
    extra = 1
    raw_id_fields =("tag",)
    
    
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):

    list_display = ("title","category", "status", "published_at", "created_at")
    list_filter = ("status", "category")
    search_feilds = ("little","body")
    date_hierarchy = ("published_at")
    ordering = ("-published_at",)


    prepopulated_fields = {"slug": ("title",)}
    readonly_fields = ("created_at","updated_at")
    fieldsets = (
    ("Basic info", {"fields": ("title", "slug", "status")}),
    ("content", {"fields":("body",)}),
    ("Relations & Dates", {"fields":("category", "published_at")}),
    ("Timestamps", {"fields":("created_at", "updated_at")}),
    )

    #Inline M2M editor: hide the default M2M widget for tags

    inlines = [PostTagInline]
    exclude = ("tags",)

    #--------custom actions-------
    @admin.action(description="Mark selected posts as published")
    def mark_as_published(self,request,queryset):
        #Only update ones not already publushed
        count = queryset.exclude(status="published").update(
        status="published",
         published_at=timezone.now(),
     )
        self.message_user(request, f"{count} post(s) marked as published")

    actions = ["mark_as_Draft"]

    @admin.action(description="Mark selected posts as Draft")
    def mark_as_published(self,request,queryset):
        #Only update ones not already publushed
        count = queryset.exclude(status="draft").update(
        status="draft",
         published_at=timezone.now(),
        )
        self.message_user(request, f"{count} post(s) marked as published")

    actions = ["mark_as_Draft"]

#simple registerations for category & tag
admin.site.register(Category)
admin.site.register(Tag)