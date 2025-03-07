from django.contrib import admin
from .models import ArticleCategory, Article

# Register your models here.

class ArticleInLine(admin.TabularInline):
    model = Article

class ArticleCategoryAdmin(admin.ModelAdmin):
    inlines = [ArticleInLine,]

admin.site.register(ArticleCategory, ArticleCategoryAdmin)
