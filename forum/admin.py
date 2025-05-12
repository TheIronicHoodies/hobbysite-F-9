from django.contrib import admin
from .models import ThreadCategory, Thread

class ThreadCategoryAdmin(admin.ModelAdmin):
    search_fields = ("name",)  
    list_display = ("name", "description")  
    ordering = ("name",) 

class ThreadAdmin(admin.ModelAdmin):
    search_fields = ("title", "entry") 
    list_display = ("title", "category", "created_on", "updated_on")  
    list_filter = ("category",)  
    ordering = ("-created_on",)  

admin.site.register(Thread, ThreadCategoryAdmin)
admin.site.register(Thread, ThreadAdmin)