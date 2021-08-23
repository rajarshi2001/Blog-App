from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth.models import User
from .models import Post, Comment, Category
class signUpForm(UserCreationForm):
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your Password'}))
    password2 = forms.CharField(label="Confirm Password(Again)", widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Your Password'}))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username']

        labels = {'first_name': 'First Name', 'last_name': 'Last Name', 'email': 'Email Address', 'username': 'Username'}
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Last Name'}),
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Username'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter Email Address'}),
        }

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'autofocus': True, 'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

class PostForms(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['cat', 'name', 'desc', 'post_img']
        labels = {'cat': 'Select Category', 'name': 'Write Topic', 'desc': 'Write Blog', 'post_img': 'Upload Picture'}
        widgets={'cat': forms.Select(attrs={'class':'form-control', 'placeholder': 'Choose Category'}), 
        'name': forms.TextInput(attrs={'class': 'form-control'}),
        'desc': forms.Textarea(attrs={'class': 'form-control'}),
        'post_img': forms.ClearableFileInput(attrs={'class': 'form-control'})}

class CommentForms(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['client_comment']
        labels = {'client_comment': 'Add Comment'}
        widgets = {'client_comment': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Add Your valuable commnent'})}

class changePasswordForm(PasswordChangeForm):
    old_password = forms.CharField(label='Current Password', widget=forms.PasswordInput(attrs={'class':'form-control', 'autofocus':True}))
    new_password1 = forms.CharField(label='Set New Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    new_password2 = forms.CharField(label='Confirm Password(Again)', widget=forms.PasswordInput(attrs={'class':'form-control'}))

class CategoryForms(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['title', 'cat_img']
        labels = {'title': 'Create Title', 'cat_img': 'Upload Category Image'}
        widgets = {'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter title'}), 
        'cat_img': forms.ClearableFileInput(attrs={'class': 'form-control'})}
        
        
