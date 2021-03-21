from django.contrib import admin
from .models import Article

# Register your models here.
# admin 위한 기능을 제공하는 Class 제작중
class ArticleAdmin(admin.ModelAdmin):
    # 우리가 만든 필드명들
    list_display = ['pk', 'title', 'content', 'created_at', 'updated_at', ]  # Tuple or list 작성

# admin site에 등록하겠다. 내가 만든 Article 모델을
admin.site.register(Article, ArticleAdmin)