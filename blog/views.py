from django.shortcuts import render, HttpResponseRedirect
from .models import Category, Post, Comment
from .forms import signUpForm, LoginForm, PostForms, CommentForms, changePasswordForm, CategoryForms
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group


def Home_View(request):
        category = Category.objects.all()
        return render(request, 'home.html', {'category': category})




def filter_topic(request, title, id=None):
    if request.user.is_authenticated:
        topics = Post.objects.filter(cat__title=title)
        return render(request, 'blogtopic.html', {'title': title, 'topics': topics})
    else:
        messages.warning(request, 'Please Login First !!')
        return HttpResponseRedirect('/userLogin/')

def blog_view(request, title, id):
    if request.user.is_authenticated:
        blogs = Post.objects.get(pk=id)
        return render(request, 'blogs.html', {'blogs': blogs})
    else:
        messages.warning(request, 'Please Login First !!')
        return HttpResponseRedirect('/userLogin/')

def sign_up_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            forms = signUpForm(data=request.POST)
            if forms.is_valid():
                user = forms.save()
                group = Group.objects.get(name='Clients')
                user.groups.add(group)
                forms = signUpForm()
                messages.success(request, 'You are registered successfully !!')
        else:
            forms = signUpForm()
        return render(request, 'signup.html', {'forms': forms})
    else:
        return HttpResponseRedirect('/')

def login_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            forms = LoginForm(data=request.POST)
            if forms.is_valid():
                uname = forms.cleaned_data['username']
                pwd = forms.cleaned_data['password']
                user = authenticate(username=uname, password=pwd)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'You are logged in successfully !!')
                    return HttpResponseRedirect('/')
        else:
            forms = LoginForm()
        return render(request, 'userlogin.html', {'forms': forms})
    else:
        return HttpResponseRedirect('/')

def post_view(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            forms = PostForms(data=request.POST, files=request.FILES)
            if forms.is_valid():
                user = request.user
                reg = forms.save(commit=False)
                reg.user = user
                reg.save()
                messages.success(request, 'Your Post has been added successfully!!')
                forms = PostForms()
        else:
            forms = PostForms()
        return render(request, 'AddPost.html', {'forms': forms})
    else:
        return HttpResponseRedirect('/userLogin/')

def dashboard_view(request):
    if request.user.is_authenticated:
        uname = request.user.username
        indPosts = Post.objects.filter(user__username=uname)
        return render(request, 'dashboard.html', {'indPosts': indPosts})
    else:
        return HttpResponseRedirect('/userLogin/')

def edit_view(request, id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            posts =  Post.objects.get(pk=id)
            forms = PostForms(data=request.POST, files=request.FILES, instance=posts)
            if forms.is_valid():
                forms.save()
                return HttpResponseRedirect('/')
        else:
            posts =  Post.objects.get(pk=id)
            forms = PostForms(instance=posts)
        return render(request, 'EditPost.html', {'forms':forms}) 
    else:
        return HttpResponseRedirect('/userLogin/')
def addComment_view(request,id1, id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            forms = CommentForms(data=request.POST)
            if forms.is_valid():
                reg = forms.save()
                c_post = Post.objects.get(pk=id1)
                print(c_post.name)
                reg.client_allposts = c_post
                reg.send = request.user.username
                ded_user = User.objects.get(pk=id)
                print(ded_user.username)
                reg.users = ded_user
                reg.save()
                messages.success(request, 'Your comment has been sent successfully !!')
        else:
            forms = CommentForms()
        return render(request, 'addComments.html', {'forms': forms})
    else:
        return HttpResponseRedirect('/userLogin/')
def viewComment_view(request, name, id):
    coms = Comment.objects.filter(client_allposts__name=name).filter(users=request.user)
    if request.user.is_authenticated:
        if request.method == 'POST':
            forms = CommentForms(data=request.POST)
            sendName = request.POST['sendName']
            if forms.is_valid():
                reg = forms.save()
                c_post = Post.objects.get(name=name)
                reg.client_allposts = c_post
                reg.send = request.user.username
                ded_user = User.objects.get(username=sendName)
                reg.users = ded_user
                reg.save()
                messages.success(request, 'Reply sent Successfully')
        else:
            forms = CommentForms()
        return render(request, 'viewcomments.html', {'coms': coms, 'nCom':len(coms), 'forms': forms})
    else:
        return HttpResponseRedirect('/userLogin/')
def password_change_view(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            forms = changePasswordForm(data=request.POST,user=request.user)
            if forms.is_valid():
                forms.save()
                return HttpResponseRedirect('/userLogin/')
        else:
            forms = changePasswordForm(user=request.user)
        return render(request, 'changePassword.html', {'forms':forms})
    else:
        return HttpResponseRedirect('/userLogin/')
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/userLogin/')

def add_category(request):
    if request.user.is_authenticated:
        allCat = []
        cat = Category.objects.all()
        for c in cat:
            allCat.append(c.title)
        if request.method == 'POST':
            forms = CategoryForms(data=request.POST, files=request.FILES)
            if forms.is_valid():
                title = forms.cleaned_data['title']
                if title  not in allCat:
                    forms.save()
                    messages.success(request, 'Category has been added successfully !!')
                else:
                    messages.error(request, 'Category is already present !!')
        else:
            forms = CategoryForms()
            
        return render(request, 'addCategory.html', {'forms':forms})
    else:
        return HttpResponseRedirect('/userLogin/')

def del_cat(request, id):
    if request.user.is_authenticated:
        pi = Category.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/userLogin/')

def blog_delete(request, id):
    if request.user.is_authenticated:
        pi = Post.objects.get(pk=id)
        pi.delete()
        messages.success(request, 'Blog deleted successfully!!')
        return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/userLogin/')


