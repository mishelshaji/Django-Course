from django import forms
from django.forms import fields
from django.contrib.auth import get_user_model


class UserDetailForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'email']
        widgets = {
            'first_name': forms.TextInput(
                attrs={'class':'form-control'}
            ),
            'last_name': forms.TextInput(
                attrs={'class':'form-control'}
            ),
            'email': forms.TextInput(
                attrs={'class':'form-control'}
            ),
        }