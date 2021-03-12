from django.db import models
from django.utils import timezone

# Create your models here.
class Article(models.Model):  # 첫글자 대문자, Model 불러오며 단수형작성
    # models 상속 받아 설계도 작성
    # title, content = Column(모델 필드)
    # charfield = 길이에 제한이 있는 TextField
    title = models.CharField(max_length=10) # Column = 필드명, 모델필드생성
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, default=timezone.now())  # 작성일. 처음 저장될때 시간만 기록을 True로
    updated_at = models.DateTimeField(auto_now=True, default=timezone.now())   # 수정일. 저장될때마다 시간 기록을 True로
