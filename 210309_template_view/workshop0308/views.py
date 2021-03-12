# Create your views here.

from django.shortcuts import render
import random

# Create your views here.
def lotto(request):
    lotto = sorted(random.sample(range(1,  46), 6))
    data = {
        'lotto': lotto,
        'greeting': 'Hello SSAFY!'
    }
    return render(request, 'workshop0308/lotto.html', data)
    # 요청을 파일로 보내준다, 넘겨줄 데이터가 3번쨰 무조건 dict형태로