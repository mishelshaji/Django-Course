from django.urls import path
from .views import *

urlpatterns = [
    path('category/create/', create_category, name="admin_create_category")
]