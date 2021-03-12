from django.shortcuts import render, redirect
from .models import Board
# Create your views here.

def index(request):
    boards = Board.objects.all()
    context = {
        'boards' : boards
    }
    return render(request, 'articles/index.html', context)


def detail(request, pk):
    board = Board.objects.get(pk=pk)
    context = {
        'board': board,
    }
    return render(request, 'articles/detail.html', context)

def new(request):
    return render(request, 'articles/new.html')

def create(request):
    board = Board()
    board.title = request.GET.get('title')
    board.content = request.GET.get('content')
    board.save()
    return redirect('detail', pk=board.pk)  # detail은 주소 사이에 추가될 값 articles/detail/pk가 여기선 주소

