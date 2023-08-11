from django import forms
from django.contrib.auth.models import User
from .models import Profile


class UserCreationForm(forms.ModelForm):
    username = forms.CharField(label='UseName', max_length=3,help_text='UserName should not contain Spaces')
    email = forms.EmailField(label='Email')
    password1 = forms.CharField(
        label='Password', widget=forms.PasswordInput(), min_length=8)
    password2 = forms.CharField(
        label='Confirm Password ', widget=forms.PasswordInput(), min_length=8)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password1'] != cd['password2']:
            raise forms.ValidationError('Not Correct')
        return cd['password2']

    def clean_username(self):
        cd = self.cleaned_data
        if User.objects.filter(username=cd['username']).exists():
            raise forms.ValidationError('UserName already Exists ')
        return cd['username']


class LoginForm(forms.ModelForm):
    username = forms.CharField(label='UserName')
    password = forms.CharField( label='Password', widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'password')


class UserUpdateForm(forms.ModelForm):
     username = forms.CharField(label='UseName')
     email = forms.EmailField(label='Email')

class Meta:
        model = User
        fields = ('username','email')


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('image',)