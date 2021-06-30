from django.http.response import HttpResponseNotFound
from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from .models import *
from .forms import *
from django.contrib import messages
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy

# Create your views here.
def create_category(request):
    if request.method == 'GET':
        context = {}
        context['form'] = CategoryForm()
        return render(request, 'administrator/category/create.html', context)

    elif request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "New Category Created")
            return redirect('admin_list_category')
        else:
            context = {}
            context['form'] = form
            return render(request, 'administrator/category/create.html', context)

def list_category(request):
    categories = Category.objects.all()
    context = {}
    context['data'] = categories
    return render(request, 'administrator/category/list.html', context)

def update_category(request, id):
    category = get_object_or_404(Category, id=id)

    if request.method == 'GET':
        context = {}
        context['form'] = CategoryForm(instance=category)
        return render(request, 'administrator/category/update.html', context)         
    else:
        form = CategoryForm(data=request.POST, instance=category)
        if form.is_valid():
            form.save()
            messages.success(request, "Category updated")
            return redirect('admin_list_category')
        else:
            context = {}
            context['form'] = form
            return render(request, 'administrator/category/update.html', context)

def delete_category(request, id):
    category = get_object_or_404(Category, id=id)
    category.delete()
    messages.success(request, "Category deleted")
    return redirect('admin_list_category')


class PostCreateView(CreateView):
    model = Post
    template_name = "administrator/post/create.html"
    success_url = reverse_lazy('admin_list_post')
    form_class = PostForm

class PostListView(ListView):
    model = Post
    template_name = "administrator/post/list.html"
    context_object_name = 'data'

class PostUpdateView(UpdateView):
    model = Post
    template_name = "administrator/post/update.html"
    pk_url_kwarg = 'id'
    form_class = PostForm
    # success_url = reverse_lazy('admin_list_post')

    def get_success_url(self):
        return reverse('admin_list_post')

class PostDeleteView(DeleteView):
    model = Post
    template_name = "administrator/post/delete.html"
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('admin_list_post')
