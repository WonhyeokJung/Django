from django.urls import path
from . import views

app_name = 'appname'
urlpatterns = [
    # practicce/'' => 목록 보여주기 HTML(전체조회)
    path('', views.index, name='index'),
    # practice/1 => 1번 학생 정보 보여주기 HTML(단일조회)
    path('<int:pk>', views.detail, name='detail'),
    #practice/new/ => 새로운 데이터 입력용 HTML(생성 준비단계)
    path('new/', views.new, name='new'),
    # practice/create/ => 사용자 입력 데이터 처리
    path('create/', views.create, name='create'),
    
    # practice/<int:pk>/edit/ => 기존의 데이터를 수정할 HTML
    path('<int:pk>/edit/', views.edit, name='edit'),
    # practice/<int:pk>/update/ => 사용자 입력 데이터 처리
    path('<int:pk>/update/', views.update, name='update'),
    # practice/<int:pk>/delete/=> 데이터 삭제(그냥 버튼 하나 주면 끝)
    path('<int:pk>/delete/', views.delete, name='delete'),
]   