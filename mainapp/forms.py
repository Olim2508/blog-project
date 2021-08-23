from django import forms
from django.forms import fields, widgets
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'body', 'author')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'input mb-6', 'name': 'title', 'placeholder': 'Title'}),
            'body': forms.Textarea(attrs={'class': 'textarea', 'name': 'body', 'placeholder': 'Body'})
}

    








# class RegisterForm(UserCreationForm):
#     username = forms.CharField( required=True, widget=forms.TextInput(attrs={'class' : 'control input'}))
#     password1 = forms.CharField(label='Password', required=True, widget=forms.PasswordInput(attrs={'class' : 'control input'}))
#     password2 = forms.CharField(label='Confirm the password', required=True, widget=forms.PasswordInput(attrs={'class' : 'control input'}))
#     email = forms.EmailField( required=True, widget=forms.TextInput(attrs={'class' : 'control input'}))
#     first_name = forms.CharField( required=True, widget=forms.TextInput(attrs={'class' : 'control input'}))
#     last_name = forms.CharField( required=True, widget=forms.TextInput(attrs={'class' : 'control input'}))


#     class Meta:
#         model = User
#         fields = ('first_name', 'last_name', 'email', 'username', 'password1', 'password2')

#     def save(self, commit=True):
#         user = super().save(commit=False)
#         user.email = self.cleaned_data['email']
#         user.first_name = self.cleaned_data['first_name']
#         user.last_name = self.cleaned_data['last_name']

#         if commit:
#             user.save()
#             return user