from django import forms
from .models import Reservation

# 상수로 변경 말라고 ALL 대문자
BIRTH_YEAR_CHOICES = ['1980', '1981', '1982']
FAVORITE_COLORS_CHOICES = [
    ('blue', '파랑'),  # value(서버에서 받아보는 값, 색깔인식), 사용자에게 보여지는값
    ('green', 'Green'),
    ('black', 'Black'),
]

class ReservationForm(forms.ModelForm):
    number = forms.IntegerField(min_value=2, required=False, widget = forms.TextInput(attrs={
        # name의 속성값에 class가 my-class로 적용됨.(BOOTSTRAP기능)
        'class':'form-control', # form-control이라는 속성값을 줌
        'placeholder':'숫자만 입력하세요',
    })) # 모델폼에서 제약조건 주는법 / required 값이 없다면 그냥 Null값 반환
    # 원래 없던 field를 준다면? 새로 생김 / BUT 저장은 안됨. MODEL에 FIELD가 없으니까
    oh = forms.CharField()
    my = forms.CharField(widget=forms.Textarea) # TextArea로 출력되어나옴

    # django widgets에서 연습삼아 따옴. 검증은 하지만, DB에 없으므로 저장을 안함.
    birth_year = forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES))
    favorite_colors = forms.MultipleChoiceField(
        required=False, # 값 없어도 돼(선택사항)
        widget=forms.CheckboxSelectMultiple, # 위젯 forms.RadioSelect로도 해보자
        choices=FAVORITE_COLORS_CHOICES,
    )
    class Meta:
        model = Reservation
        fields = '__all__'