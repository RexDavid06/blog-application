from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Post, Profile

class SignupForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in (self.fields['username'], self.fields['password1'], self.fields['password2']):
            field.help_text = None
            field.widget.attrs.update({'class': 'form-control '})


class CreatePostForm(forms.ModelForm):
    class Meta:
        model =Post
        fields = ['title', 'content']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in (self.fields['username'], self.fields['email']):
            field.help_text = None
            field.widget.attrs.update({'class': 'form-control '})