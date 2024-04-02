from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import Event, User


class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['name', 'username', 'email', 'country', 'contact_number', 'sports_category', 'password1', 'password2']


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['name', 'username', 'email', 'bio']
