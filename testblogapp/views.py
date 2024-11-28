from django.shortcuts import render, redirect
from .forms import SignupForm, CreatePostForm, ProfileUpdateForm, UserUpdateForm
from .models import Post
from django.contrib.auth import logout


# Create your views here.
def log_out(request):
    logout(request)
    return redirect('login')


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignupForm()
    return render(request, 'registration/signup.html', {"form":form})


def index(request):
    posts = Post.objects.all()
    if request.method == 'POST':
        create_post = CreatePostForm(request.POST)
        if create_post.is_valid():
            instance = create_post.save(commit=False)
            instance.user = request.user
            instance.save()
            return redirect('index')
    else:
        create_post = CreatePostForm()
         
    context = {
        "posts":posts,
        "create_post": create_post,
    }
    return render(request, 'base/index.html', context)

def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST or None, instance=request.user)
        p_form = ProfileUpdateForm(request.POST or None, request.FILES or None, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('profile')
    else:
        u_form = UserUpdateForm(request.POST or None, instance=request.user)
        p_form = ProfileUpdateForm(request.POST or None, request.FILES or None, instance=request.user.profile)
        context = {
            "u_form":u_form,
            "p_form": p_form
        }
    return render(request, 'registration/profile.html', context)

