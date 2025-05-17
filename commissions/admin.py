from django.contrib import admin
from .models import Commission, Comment, Job, JobApplication

# Register your models here.
class CommentInline(admin.TabularInline):
    model = Comment
    
class CommissionAdmin(admin.ModelAdmin):
    model = Commission
    inlines = [CommentInline,]

class CommentAdmin(admin.ModelAdmin):
    model = Comment
    
class JobAdmin(admin.ModelAdmin):
    model = Job
    
    
class JobApplicationAdmin(admin.ModelAdmin):
    model = JobApplication

admin.site.register(Commission, CommissionAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Job, JobAdmin)
admin.site.register(JobApplication, JobApplicationAdmin)