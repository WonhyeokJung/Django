from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_GET, require_POST, require_http_methods, require_safe
from .models import Reservation
from .forms import ReservationForm
# Create your views here.

@require_http_methods(['GET', 'POST']) # 이 요청만 받겠다.
def new(request):
    form = ReservationForm()
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save()
            return redirect('board:detail', reservation.pk)
    else:
        form = ReservationForm()
    context = {  # 에러시 여기서 context해서 보여줄수 있음(is_valid의 효과. 저기서 에러메세지와 맞은 데이터내용을 다 갖고 있음.)
        'form' : form,
    }
    return render(request, 'board/new.html', context)

@require_GET
def index(request):
    # 순서 역순으로 가져옴. 출력이 역순으로 된다.
    reservations = Reservation.objects.order_by('-pk') # 쿼리문 날릴때 역으로 pk가져옴
    context = {
        'reservations': reservations,
    }
    return render(request, 'board/index.html', context)

@require_safe
def detail(request, pk):
   # reservation = Reservation.objects.get(pk=pk) 대처 404에러 커버 되게
   reservation = get_object_or_404(Reservation, pk=pk) # 오른쪽 pk가 함수매개인자 path와 명칭통일이 필요
   context = {
       'reservation':reservation,
   }
   return render(request, 'board/detail.html', context)

@require_http_methods(['GET', 'POST'])
def edit(request, pk):
    reservation = get_object_or_404(Reservation, pk=pk)
    if request.method == 'POST':
        # form = ReservationForm(request.POST) # 생성
        # 기존데이터와 연관있음을 명시
        form = ReservationFrom(request.POST, instance=reservation)
        if form.is_valid():
            reservation = form.save()
            return redirect('board:detail', reservation.pk)
    else:
        form = ReservationForm(instance=reservation)
    context = {  # 에러시 여기서 context해서 보여줄수 있음(is_valid의 효과. 저기서 에러메세지와 맞은 데이터내용을 다 갖고 있음.)
        'form' : form,
    }
    return render(request, 'board/edit.html', context)

@require_POST
def delete(request, pk):
    reservation = get_object_or_404(Reservation, pk=pk)
    reservation.delete()
    return redirect('board:index')