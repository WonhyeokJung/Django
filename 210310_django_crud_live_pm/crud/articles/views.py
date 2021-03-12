from django.shortcuts import render
from .models import Article

# Create your views here.
def index(request):
    # 데이터 조회후 index.html로 보내주기
    # 모든 게시글을 조회
    articles = Article.objects.all()
    context = {
        'articles' : articles,
    }
    return render(request, 'articles/index.html', context)