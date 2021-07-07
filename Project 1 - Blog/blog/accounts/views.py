from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout

# Create your views here.
def register(request):
    if request.method == 'GET':
        context = {}
        context['form'] = UserCreationForm()
        return render(request, 'accounts/register.html', context)
    elif request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            messages.success(request, 'Account created successfully.')
            form.save()
            return redirect('user_home')
        else:
            context = {}
            context['form'] = form
            return render(request, 'accounts/register.html', context)

def user_login(request):
    # if request.user.is_authenticated:
    #     print("Authenticated")
    #     print(request.user.username)
    if request.method == 'GET':
        context = {}
        context['form'] = AuthenticationForm()
        return render(request, 'accounts/login.html', context)
    elif request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            login(request, user)
            return redirect('user_home')
        else:
            context = {}
            context['form'] = form
            messages.error(request, "Invalid username or password")
            return render(request, 'accounts/login.html', context)

def user_logout(request):
    logout(request)
    return redirect('user_home')