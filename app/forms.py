"""
Definition of forms.
"""

from django import forms
from app import models
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User

class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'User name'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Password'}))

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'First Name'}))
    last_name = forms.CharField(max_length=30, required=False, widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'Last Name'}))
    email = forms.EmailField(max_length=254, widget=forms.EmailInput({
                                   'class': 'form-control',
                                   'placeholder': 'Email ID'}))
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'User Name'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )

class CreateCourse(forms.ModelForm):
    class Meta:
        model= models.Course
        fields = []
