from django.shortcuts import render,redirect
from .models import Article
# Create your views here.

def index(request):
    articles = Article.objects.all()
    context = {
        'articles' : articles,
    }
    return render(request, 'articles/index.html',context)

def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)

def new(request):
    return render(request, 'articles/new.html')

def create(request):
    # request.Get
    titles = request.POST.get('title')
    contents = request.POST.get('content')
    # 첫 번재 방법
    article = Article()
    article.title = titles
    article.content = contents
    article.save() # 세이브가 됐으니, id가 부여된 인스턴스화 됐다.
    
    # 두번 째 방법 : 가장 좋은 방법, 유효성 검증이 있어야되기 때문
    #article = Article(title = titles, content=contents)
    # article.save()
    # 세번째 방법
    #Article.objects.create(title=titles, content=contents)

    # return render(request, 'articles/create.html')
    return redirect('articles:detail', article.pk)

def delete(request, pk):
    # 몇번 글 삭제할 건데? -> 조회
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('articles:index')

def edit(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article' : article
    }
    return render(request, 'articles/edit.html', context)

def update(request, pk):
    # 몇 번 게시글 수정? -> 조회
    article = Article.objects.get(pk=pk)
    
    titles = request.POST.get('title')
    contents = request.POST.get('content')

    # article = Article(title = titles, content=contents)
    # 첫 번째 방법 형식으로 update
    article.title = titles
    article.content = contents
    article.save()

    return redirect('articles:detail', article.pk)