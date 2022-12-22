from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import AddPostForm
from .forms import NewUserForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User

def home(request):
    return render(request, "pages/home.html")

def postt(request):
    posts = Post.objects.all().order_by('postDate')
    return render(request, "pages/posts.html", {
        'posts': posts
    })


def addPost(request):
    if request.method == "POST":
        form = AddPostForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.userPost = request.user
            form.save()
            return redirect('postt')
    else:
        form = AddPostForm()
    return render(request, "pages/add-post.html", {
        'form': form
    })


def postDetail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, "pages/post-detail.html", {
        'post': post
    })


def deletePost(request, pk):
    post = Post.objects.get(pk=pk)
    if request.user == post.userPost:
        if request.method == 'POST':
            Post.objects.filter(pk=pk).delete()
            return redirect('postt')

    return render(request, "pages/delete-post.html", {
        'post': post
    })

def editPost(request, pk):
    post = get_object_or_404(Post, pk=pk)
    form = AddPostForm(request.POST or None, request.FILES or None, instance=post)
    if request.user == post.userPost:
        if request.method == "POST":
            if form.is_valid():
                form.save()
                return redirect("postDetail", pk=post.pk)

    return render(request, "pages/edit-post.html", {
        'post': post,
        'form': form,
    })



def signUp(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("home")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    else:
        form = NewUserForm()
    return render(request, "pages/sign-up.html", {
        'form': form
    })

def logIn(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("home")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
    return render(request, "pages/log-in.html", {
        'form': form
    })

def logoutUser(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect("home")