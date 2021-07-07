from django.urls import path
from .views import *

urlpatterns = [
    path('login/', user_login, name='accounts_login'),
    path('register/', register, name='accounts_register'),
    path('logout/', user_logout, name='accounts_logout'),
]