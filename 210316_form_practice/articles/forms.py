from django import forms
from .models import Article

"""
Why do we use Form ?
1. Data Validation
2. For making HTML code easier
"""
# forms.Form => 특정 모델과 연동 X. 단순히 데이터검증 /HTML 생성용
class ContactForm(forms.Form):
    name = forms.CharField(min_length=2, max_length=5)
    email = forms.EmailField()
    age = forms.IntegerField(min_value=3, max_value=100)
    # content = forms.CharField() 
    content = forms.CharField(widget=forms.Textarea)

class ArticleForm(forms.ModelForm):
    
    class Meta:
        model = Article
        fields = '__all__'