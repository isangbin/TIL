from .models import Post
from .forms import PostForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    posts = Post.objects.all()
    context = {
        'posts': posts,
    }
    return render(request, 'posts/index.html', context)


@login_required
def create(request):
    form = PostForm(request.POST, request.FILES)
    if request.method == 'POST':
        if form.is_valid():
            post = form.save()
            return redirect('posts:index')
    else:
        form = PostForm()
    
    context = {
        'form': form,
    }
    return render(request, 'posts/form.html', context)


def delete(request, pk):
    if request.user.is_authenticated:
        # if request.user == post.user:
        post = Post.objects.get(pk=pk)
        post.delete()
        return redirect('posts:index')
    return redirect('accounts:login')


@login_required
def update(request, pk):
    post = Post.objects.get(pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('posts:index')
        else:
            form = PostForm(instance=post)
    
    context = {
        'post': post,
        'form': form,
    }
    return render(request, 'posts/form.html', context)