from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='user_home'),
    path('about/', about, name='user_about'),
    path('contact/', contact, name='user_contact'),
]