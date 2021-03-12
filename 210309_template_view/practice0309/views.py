from django.shortcuts import render
from django.http.response import HttpResponse
import requests
import random
import datetime

# Create your views here.

def var_route(request, value):
    # context = {
    #     'value': value
    # }
    return HttpResponse(value)
    # return render(request, 'lotto.html', context)
    
def lotto(request, value):
    # 1. 현실 로또 번호를 가져온다.
    # + fstring 통한 주소변경
    url = f'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo={value}'
    # url 값 요청 + json으로 가공
    lotto_dict = requests.get(url).json()

    # 이번 회차 당첨 번호
    win_num = [
        lotto_dict['drwtNo1'],
        lotto_dict['drwtNo2'],
        lotto_dict['drwtNo3'],
        lotto_dict['drwtNo4'],
        lotto_dict['drwtNo5'],
        lotto_dict['drwtNo6'],
    ]
    bonus_num = lotto_dict['bnusNo']

    # 등수 1, 2, 3, 4, 5, 꽝
    result = [0]*6

    # 로또 buy회 실행
    buy = 1000
    for i in range(buy):
        lotto = sorted(random.sample(range(1, 46), 6))

        count = 0
        for win in win_num:
            for my_num in lotto:
                if win == my_num:
                    count += 1
        # 추첨
        if count == 6:
            result[0] += 1
        elif count == 5 and bonus_num in lotto:
            result[1] += 1
        elif count == 5:
            result[2] += 1
        elif count == 4:
            result[3] += 1
        elif count == 3:
            result[4] += 1
        else:
            result[5] += 1

    # html에 전송할 데이터
    context = {
        'num': lotto_dict,  # 이렇게 이름 다르게 X
        'result': result,
        'buy': buy,
    }

    return render(request, 'practice0309/lotto.html', context)

# 사용자가 입력할 form & input용 **HTML을 제공**
def ping(request):
    return render(request, 'practice0309/ping.html')

# 사용자 입력 데이터를 활용하는 view 함수
def pong(request):
    #딕셔너리
    print(request.GET) # <QueryDict: {'kor-name': ['가나다'], 'eng-name': ['ganada']}>

    # 온 데이터를 꺼내는 request.GET form의 method의 GET임
    # USER, GET, POST, COOKIE, META 등등 많음.\
    # get() 딕셔너리의 값을 가져옴.
    # request.GET['kor-name'] 대괄호는 key없으면 에러, get은 None을 Return
    # request.GET['eng-name']도 가능
    kor_name = request.GET.get('kor-name')
    eng_name = request.GET.get('eng-name')
    today = datetime.datetime.now()
    context = {
        'kor_name':kor_name,
        'eng_name':eng_name,
        'today':today
    }
    return render(request, 'practice0309/pong.html', context)
    # 네임스페이싱 practice0309/pong.html
    # {% url app_name:pong %} 이런식으로. 나중에 배움