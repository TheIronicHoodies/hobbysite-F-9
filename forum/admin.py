from django.contrib import admin
from .models import PostCategory, Post

class PostCategoryAdmin(admin.ModelAdmin):
    search_fields = ("name",)  
    list_display = ("name", "description")  
    ordering = ("name",) 

class PostAdmin(admin.ModelAdmin):
    search_fields = ("title", "entry") 
    list_display = ("title", "category", "created_on", "updated_on")  
    list_filter = ("category",)  
    ordering = ("-created_on",)  

admin.site.register(PostCategory, PostCategoryAdmin)