from django import forms

from todo.models import Profile
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = "__all__"

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = "__all__"
