from django.db import models

# Create your models here.
# Table 생성
class Article(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)  # 작성일. 처음에만 수정
    updated_at = models.DateTimeField(auto_now=True)  # 수정일. 새로 데이터갱신시 수정
    