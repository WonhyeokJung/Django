"""my_pjt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
# dev 모드(DEBUG = TRUE false일땐 빈 리스트)에서는 사용자 업로드 미디어를 서빙하기 위해 아래 코드가 필요합니다.
# settings.py에 MEDIA_URL값이 있어, 업로드는 가능하게 되었다. 하지만
# 사용자가 실제 웹 페이지 내에서 이 파일을 조회 할 수 있도록 하기위해선 업로드 된 파일에 대한 URL을 생성 해주는 설정
# 그를 위해 사용 코드
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('uploader/', include('uploader.urls')),
    # path('static/<str:filename>/', ),  # 어디서나 가져올수있는 자료
    # 안써도되게 settings에 세팅되어있음
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# 위코드는 path('media/', 'BASE_DIR/media' 폴더를 찾아라 의미)
