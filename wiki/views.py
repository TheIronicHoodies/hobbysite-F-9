from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Article, ArticleCategory, Comment, ImageGallery
from .forms import ArticleForm, CommentForm, imageGalleryForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import FormMixin


class ArticleListView(ListView):
    model = ArticleCategory
    template_name = 'wiki_list.html'


class ArticleDetailView(FormMixin, DetailView):
    model = Article
    template_name = 'wiki_detail.html'
    form_class = CommentForm
    
    def post(self, request, *args, **kwargs):
        c = Comment()
        c.entry = request.POST.get('entry')
        c.author = self.request.user.profile
        c.article = self.get_object()
        c.save()
        return self.get(request, *args, **kwargs)


class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    template_name = 'wiki_create.html'
    form_class = ArticleForm
    redirect_field_name = 'login.html' #redirects to login
    
    def form_valid(self, form): #this automatically sets the author value from the form to the requested user's profile
        temp = form.save(commit=False)
        temp.author = self.request.user.profile
        temp.save()
        return super().form_valid(form)
    
    
class ArticleUpdateView(LoginRequiredMixin, UpdateView):
    model = Article
    template_name = 'wiki_update.html'
    form_class = ArticleForm
    redirect_field_name = 'login.html' #redirects to login


class ImageCreateView(LoginRequiredMixin, CreateView):
    model = ImageGallery
    template_name = 'wiki_image.html'
    form_class = imageGalleryForm
    redirect_field_name = 'login.html' #redirects to login