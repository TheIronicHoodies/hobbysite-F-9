"""Creates an admin panel for the forum app."""

from django.contrib import admin
from .models import ThreadCategory, Thread, Comment

class ThreadCategoryAdmin(admin.ModelAdmin):
    search_fields = ("name",)  
    list_display = ("name", "description")  
    ordering = ("name",) 

class ThreadAdmin(admin.ModelAdmin):
    search_fields = ("title", "entry") 
    list_display = ("title", "category", "created_on", "updated_on")  
    list_filter = ("category",)  
    ordering = ("-created_on",)  

class CommentAdmin(admin.ModelAdmin):
    list_display = ("thread", "author", "created_on")
    list_filter = ("created_on",)
    search_fields = ("entry",)

admin.site.register(ThreadCategory, ThreadCategoryAdmin)
admin.site.register(Thread, ThreadAdmin)
admin.site.register(Comment, CommentAdmin)