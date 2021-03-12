from django.urls import path
from . import views

# /practice0309/ 까지
urlpatterns = [
    # /practice0309/lotto
    # Variable Routing으로 주소를 동적변경
    # <> 내 변수명은 view의 함수 변수명과 같아야한다.
    path('dinner/<str:dinner_menu>/<int:people>', views.dinner, name='dinner'),
    
]