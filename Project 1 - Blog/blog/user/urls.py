from django.urls import path
from .views import *

urlpatterns = [
    path('', PostListView.as_view(), name='user_home'),
    path('<slug:slug>/', PostDetailView.as_view(), name='user_post_detail'),
    path('about/', about, name='user_about'),
    path('contact/', contact, name='user_contact'),
]