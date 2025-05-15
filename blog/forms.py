from django import forms
from .models import Article, Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['entry']
        widgets = {
            'created_on': forms.TextInput(attrs={'type': 'datetime-local'}),
            'updated_on': forms.TextInput(attrs={'type': 'datetime-local'}),
        }

class ArticleCreateForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'category', 'entry']

class ArticleUpdateForm(forms.ModelForm):
    class Meta:
        model = Article
        exclude = ['author', 'created_on', 'updated_on']