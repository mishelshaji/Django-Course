from django.shortcuts import render, HttpResponse
from django.views.generic import ListView, DetailView
from administrator.models import Post

# Create your views here.
class PostListView(ListView):
    model = Post
    template_name = "user/home.html"
    context_object_name = 'post_list'
    paginate_by = 6

class PostDetailView(DetailView):
    model = Post
    template_name = "user/post_detail.html"
    slug_url_kwarg = 'slug'

def about(request):
    return render(request, 'user/about.html')

def contact(request):
    return render(request, 'user/contact.html')
