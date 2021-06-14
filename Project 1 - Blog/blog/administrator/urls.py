from django.urls import path
from .views import *

urlpatterns = [
    path('category/', list_category, name="admin_list_category"),
    path('category/create/', create_category, name="admin_create_category"),
    path('category/update/<int:id>/', update_category, name="admin_update_category"),
]