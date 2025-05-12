from django import forms
from .models import Article, Comment

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__'
        widgets = { 'created_on': forms.TextInput(attrs={ 'type' : 'datetime-local'}),
                   'updated_on': forms.TextInput(attrs={'type' : 'datetime-local'})}

 
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('entry',)
        widgets = { 'created_on': forms.TextInput(attrs={ 'type' : 'datetime-local'}),
                   'updated_on': forms.TextInput(attrs={'type' : 'datetime-local'})}