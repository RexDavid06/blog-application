from django.shortcuts import render, redirect
from .forms import SignupForm, CreatePostForm, ProfileUpdateForm, UserUpdateForm, PostUpdateForm
from .models import Post
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

from django.contrib.auth.views import LoginView
from django.utils.decorators import method_decorator
from .decorators import anonymous_required


# Create your views here.

def log_out(request):
    logout(request)
    return redirect('login')

@anonymous_required
def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignupForm()
    return render(request, 'registration/signup.html', {"form":form})

@login_required(login_url='login')
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

@login_required(login_url='login')
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
    return render(request, 'base/profile.html', context)


@login_required(login_url='login')
def post_detail(request, pk):
    posts = Post.objects.get(id=pk)
    context = {
        "posts": posts,
    }
    return render(request, 'base/post_detail.html', context)


@login_required(login_url='login')
def edit_post(request, pk):
    posts =  Post.objects.get(id=pk)
    if request.method == 'POST':
        forms = PostUpdateForm(request.POST, instance=posts)
        if forms.is_valid():
            forms.save()
            return redirect('post_detail',  pk=posts.id)
    else:
        forms = PostUpdateForm(instance=posts)
    context = {
        "posts": posts,
        "forms": forms
    }
    return render(request, 'base/edit_post.html', context)


@login_required(login_url='login')
def delete_post(request, pk):
    posts = Post.objects.get(id=pk)
    if request.method == 'POST':
        posts.delete()
        return redirect('index')
    context = {
        "posts": posts
    }
    return render(request, 'base/delete_post.html', context)









class AnonymousLoginView(LoginView):
    @method_decorator(anonymous_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
