from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegisterForm(UserCreationForm):
    username = forms.CharField( required=True, widget=forms.TextInput(attrs={'class' : 'control input'}))
    password1 = forms.CharField(label='Password', required=True, widget=forms.PasswordInput(attrs={'class' : 'control input'}))
    password2 = forms.CharField(label='Confirm the password', required=True, widget=forms.PasswordInput(attrs={'class' : 'control input'}))
    email = forms.EmailField( required=True, widget=forms.TextInput(attrs={'class' : 'control input'}))
    first_name = forms.CharField( required=True, widget=forms.TextInput(attrs={'class' : 'control input'}))
    last_name = forms.CharField( required=True, widget=forms.TextInput(attrs={'class' : 'control input'}))


    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']

        if commit:
            user.save()
            return user