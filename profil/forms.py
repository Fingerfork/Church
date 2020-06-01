from django import forms
from .models import AdvUser
from django.contrib.auth import password_validation
from django.core.exceptions import ValidationError


class ChangeUserInfoForm(forms.ModelForm):
    email = forms.EmailField(required=True,
                             label='Адрес электронной почты')

    class Meta:
        model = AdvUser
        fields = ('username', 'email', 'first_name', 'last_name', 'send_messages')