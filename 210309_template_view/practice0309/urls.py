from django.urls import path
from . import views

# /practice0309/ 까지
urlpatterns = [
    # /practice0309/lotto
    # Variable Routing으로 주소를 동적변경
    path('lotto/<int:value>', views.lotto, name='plotto'),
    # /practice0309/var_route/뭐든지들어옴/
    path('var_route/<int:value>/', views.var_route),
    # routing시 반드시 변수를 받아줘야함에 유의

    # 값을 넘겨줄때 HTML도 두개 , VIEW도 두개 필요
    #/practice0309/ping/ => <form>으로 사용자 입력받기
    path('ping/', views.ping, name='ping'), 
    #/practice0309/pong/ => 처리 결과 보여주기
    path('pong/', views.pong, name='pong'),
]
