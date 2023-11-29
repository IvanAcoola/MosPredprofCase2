from dataclasses import field
from urllib import request
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    #def __init__(self, *args, **kwargs):
        #self.fields['username'].label = 'Имя пользлователя'
        #self.fields['email'].label = 'Электронная почта'
        #self.fields['password1'].label = 'Электронная почта'
        #self.fields['password2'].label = 'Электронная почта'
        #super().__init__(*args, **kwargs)


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].label = 'Имя пользлователя'
        self.fields['email'].label = 'Электронная почта'

        #self.fields['username'].widget.attrs.update({'class':'sex'})


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image'].label = 'Изображение профиля'
