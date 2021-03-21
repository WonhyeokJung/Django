from django.shortcuts import render, redirect, get_object_or_404
from .models import Article
from .forms import ContactForm, ArticleForm

"""
1. 사용자가 /crud/contact/로 접속 => GET /crud/contact/
2. 사용자가 HTML > form에서 데이터 제출 => POST /crud/contact/ [Form태그 action칸에 내가 직접 써둬서]
3. def contact가 다시 실행되면서 elif POST문이 실행됨
4. view 함수에서 contact로 redirect 시킴 => GET /crud/contact/
"""

# Create your views here.
def contact(request):
    contact_form = ContactForm()
    context = {
        'contact_form':contact_form,
    }
    print(context)
    if request.method == 'GET':
        contact_form = ContactForm()
        context = {
            'contact_form':contact_form,
        }
        print(context)
        return render(request, 'articles/contact.html', context)
    # New와 Create역할을 혼자서 다하게 됨 POST가. SUBMIT 버튼 누르면 그 때만 POST요청이 됨.
    elif request.method == 'POST':  # POST요청 보내는 법은 method post form태그에서 버튼 눌러야만 가능
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            contact = Contact()
            contact.name = contact_form.changed_data.get()
            contact.email = contact_form.changed_data.get()
            contact.content = contact_form.changed_data.get()
            contact.save()
        else:
            # print(request.POST)
            print(contact_form)
            print(contact_form.is_valid())
            contact_form = ContactForm()
            context = {
                'contact_form':contact_form,
            }   
            # return redirect('contact')  # 다시 GET으로 보낸다.
            return render(request, 'articles/contact.html', context)

def new(request):
    form = ArticleForm()
    context = {'form':form}
    if request.method == 'GET':
        form = ArticleForm()
        context = {'form':form}
        return render(request, 'articles/new.html', context)
    elif request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
            return redirect('detail', article_pk = article.pk)
        else:
            context = {'form': form} # 이게 없으면 틀린 값을 제외하고 맞는값도 다 지워버리고 뭐에서 에러 났는지도
            # 안보여주고 그냥 초기화 시켜버리는 갓갓코드가 되어버린다. 사용자는 저장된지도 확인도 불가능
            print(1)
            return render(request, 'articles/new.html', context)

def refactored_new(request): # new 줄이기
    if request.method == 'POST':
        pass

def index(request):
    articles = Article.objects.all()
    context = {'articles':articles}
    return render(request, 'articles/index.html', context)

def detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)  # 404함수가 pk라는 인자를 받게 되어있음
    context = {'article':article}
    return render(request, 'articles/detail.html', context)

def edit(request, article_pk):
    # 기존 게시글 내용을 포함한 HTML을 만들기 위해 instance 추가
    # article = get_object_or_404(Article, pk=article_pk)
    article = Article.objects.get(pk=article_pk)

    if request.method == 'POST':
        # new와 다르게, 특정 article에 대한 내용을 request.POST로 덮어쓰기
        form = ArticleForm(request.POST, instance=article) # 내가 작성한 값 request.POST
        if form.is_valid():  # 유효성 검증
            article = form.save()
            return redirect('detail', article.pk)
    elif request.method == 'GET':
        # 기존 게시글 내용을 포함한 HTML을 만들기 위해 instance 추가. GET으로 왔으니 기존 글 들고 돌아가라
        form = ArticleForm(instance=article)
        context = {'form':form}
    return render(request, 'articles/edit.html', context)

def delete(reqeust, article_pk):
    return redirect()