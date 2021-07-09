from django.urls import path
from .views import *
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView

urlpatterns = [
    path('login/', user_login, name='accounts_login'),
    path('register/', register, name='accounts_register'),
    path('logout/', user_logout, name='accounts_logout'),
    path('detail/', UserDetailView.as_view(), name='accounts_detail'),
    path('edit/', UserUpdateView.as_view(), name='accounts_edit'),

    path('change-password/', PasswordChangeView.as_view(
        template_name = 'accounts/account/change_password.html',
        success_url = reverse_lazy('accounts_change_password_done')
    ), name='accounts_change_password'),

    path('change-password-done/', PasswordChangeDoneView.as_view(
        template_name = 'accounts/account/password_change_done.html'
    ), name='accounts_change_password_done')
]