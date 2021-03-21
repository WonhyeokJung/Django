from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    # Class명 메타는 Django에서만 특별한 의미를 가짐.
    class Meta:
        model = Article
        fields = '__all__'
        