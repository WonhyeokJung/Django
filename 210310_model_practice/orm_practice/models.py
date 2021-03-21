from django.db import models
from datetime import datetime

# Naming Convention => 단일 레코드의 이름(단수형)
class Student(models.Model):
    name = models.CharField(max_length=10)
    age = models.IntegerField()
    major = models.CharField(max_length=100)
    intro = models.TextField()  # 자기소개
    created_at = models.DateTimeField(auto_now_add=True, null = True)
    updated_at = models.DateTimeField(auto_now=True)
    
