from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_GET, require_http_methods, require_POST, require_safe
from .models import Article
from .forms import ArticleForm


# Create your views here.
@require_http_methods(['GET', 'POST'])
def new(request):
    if request.method == 'POST':
        # 보낸 이미지 파일을 따로 받아와야 함. 기본적으로 BASE_DIR에 저장됨.
        # settings.py에서 변경 가능
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save()
            return redirect('uploader:detail', article.pk)
            # 불가능 return redirect('uploader:detail', form.save().pk)
    else:
        form = ArticleForm()
    context = {'form':form}
    return render(request, 'uploader/forms.html', context)

@require_GET
def index(request):
    return render(request, 'uploader/index.html')

@require_GET
def detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    context= {
        'article':article
    }
    return render(request, 'uploader/detail.html', context)

