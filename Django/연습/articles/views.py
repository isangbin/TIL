from django.shortcuts import render, redirect
from .models import Article
# Create your views here.
def index(request):
    articles = Article.objects.all().order_by('-pk') # 최신 게시물이 최상단에 위치
    context = {
        'articles' : articles,
    }
    return render(request, 'articles/index.html', context)


def new(request):
    return render(request, 'articles/new.html')


def create(request):
    title = request.GET.get('title')
    content = request.GET.get('content')

    #1.
    # article = Article()
    # article.title = title
    # article.content = content
    # article.save()

    #2.
    article = Article(title=title, content=content)
    article.save()
    

    #3.
    # POST방식으로 받아올 땐 유효성검사를 무조건 하는데
    # 그 때 이 방법의 경우 불가능하기때문에 안쓰는게 신상에 이로움
    # Article.objects.create(title=title, content=content)
    # return render(request, 'articles/index.html')
    return redirect('articles:detail', article.pk)

    
def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article' : article
    }
    return render(request, 'articles/detail.html', context)


def delete(request, pk):
    article = Article.objects.get(pk=pk)
    
    # post방식이면 삭제 해줘.
    if request.method == 'POST':
        article.delete()
        return redirect('articles:index')
        
    # get방식이면 detail로 다시 가!    
    return render(request, 'articles/whoru.html')


def edit(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article' : article
    }
    return render(request, 'articles/edit.html', context)


def update(request, pk):
    article = Article.objects.get(pk=pk)
    article.title = request.POST.get('title')
    article.content = request.POST.get('content')
    article.save()
    return redirect('articles:detail', article.pk)
