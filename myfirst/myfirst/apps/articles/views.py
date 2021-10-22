from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import Article


def index(request):
    latest_articles = Article.objects.order_by('-pub_date')[:5]
    return render(request, 'articles/list.html', {'latest_articles': latest_articles})


def detail(request, article_id):
    try:
        a = Article.objects.get(id=article_id)
    except:
        raise Http404('Article not found')
    
    latests_coments = a.comment_set.order_by('-id')[:10]
    
    return render(request, 'articles/detail.html', {'article': a, 
                                                    'latests_comments': latests_coments})


def leave_comment(request, article_id):
    try:
        a = Article.objects.get(id=article_id)
    except:
        raise Http404('Article not found')
    
    a.comment_set.create(author_name = request.POST['name'], 
                         comment_text=request.POST['text'])
    
    return HttpResponseRedirect(reverse('articles:detail', args=(a.id,)))