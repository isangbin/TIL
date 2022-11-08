from .models import Post, Comment
from .forms import PostForm, CommentForm
from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    posts = Post.objects.all()
    comment_form = CommentForm()
    # comments = posts.comment_set.all()
    context = {
        'posts': posts,
        'comment_form': comment_form,
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


def delete(request, post_pk):
    if request.user.is_authenticated:
        # if request.user == post.user:
        post = Post.objects.get(pk=post_pk)
        post.delete()
        return redirect('posts:index')
    return redirect('accounts:login')


@login_required
def update(request, post_pk):
    post = Post.objects.get(pk=post_pk)
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


@require_POST
def comment_create(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.post = post
        comment.user = request.user
        comment.save()
    return redirect('posts:index')


@require_POST
def comment_delete(request, post_pk, comment_pk):
    if request.user.is_authenticated:
        comment = Comment.objects.get(pk=comment_pk)
        if request.user == comment.user:
            comment.delete()
    return redirect('posts:index')