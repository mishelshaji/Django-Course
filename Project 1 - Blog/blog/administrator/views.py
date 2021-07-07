from django.core import paginator
from django.http.response import HttpResponseNotFound
from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from .models import *
from .forms import *
from django.contrib import messages
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# Create your views here.
@login_required
@user_passes_test(lambda user: user.is_superuser)
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

@login_required
@user_passes_test(lambda user: user.is_superuser)
def list_category(request):
    categories = Category.objects.all().order_by('name')
    context = {}

    paginator = Paginator(categories, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context['page_obj'] = page_obj
    return render(request, 'administrator/category/list.html', context)

@login_required
@user_passes_test(lambda user: user.is_superuser)
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

@login_required
@user_passes_test(lambda user: user.is_superuser)
def delete_category(request, id):
    category = get_object_or_404(Category, id=id)
    category.delete()
    messages.success(request, "Category deleted")
    return redirect('admin_list_category')

class PostCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Post
    template_name = "administrator/post/create.html"
    success_url = reverse_lazy('admin_list_post')
    form_class = PostForm

    def test_func(self):
        return True
        # return self.request.user.is_superuser

class PostListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = "administrator/post/list.html"
    context_object_name = 'data'
    paginate_by = 20

class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    template_name = "administrator/post/update.html"
    pk_url_kwarg = 'id'
    form_class = PostForm
    # success_url = reverse_lazy('admin_list_post')

    def get_success_url(self):
        return reverse('admin_list_post')

class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = "administrator/post/delete.html"
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('admin_list_post')
