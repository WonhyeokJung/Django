from django.urls import path
from . import views

urlpatterns = [
    # DOMAIN/lotto/
    path('lotto/', views.lotto),  # URL명, 로또 함수불러올곳, name="" 임의의 이름설정

]