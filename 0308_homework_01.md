# 1. 한국 시간 나타내기 

**1-1. django 서버를 실행하고 첫 페이지에 접속했을 때 터미널에 출력된 서버 시간이 현재 한국 시간과 다른 시간으로 출력된다. 이를 한국 시간으로 바꾸려면 settings.py에 어떤 변 수 그리고 어떤 값을 할당해야 하는지 작성하시오.**

```
Settings에서 "TIME_ZONE" 을 "Asia/Seoul"로 변경한다.
```



**1-2. 추가로 settings.py에 "이 변수"가 False인 상태로 1-1번 변수를 설정하는 것은 error라 고 한다. "이 변수"는 무엇인가?**

```
정말로 모르겠습니다. USE_TZ를 False로 설정하면, DB에도 같은 시간이 된다고는 보았는데, 이와는 관계없는 것 같습니다.
```



# 2. 경로 설정하기 

**다음은 어떤 django 프로젝트의 urls.py의 모습이다. 주소 ’/ssafy’로 요청이 들어왔을 때실 행되는 함수가 pages 앱의 views.py 파일 안 ssafy 함수라면, 요청에 응답하기 위해 빈칸 __(a)__에 추가되어야 할 코드를 작성하시오.**

```
'ssafy/', views.ssafy
```



# Django Template Language 

**아래 링크를 참고하여 각 문제들을 해결하기 위한 코드를 작성하시오.**

https://docs.djangoproject.com/en/3.1/ref/templates/builtins/

1) menus 리스트를 반복문으로 출력하시오.

```
menu
```

2) posts 리스트를 반목문을 활용하여 0번 글부터 출력하시오.

```
forloop.counter0
```

3) users 리스트가 비어있다면 현재 가입한 유저가 없습니다. 텍스트를 출력하시오.

```
empty
```

4) 첫 번째 반복문일 때와 아닐 때를 조건문으로 분기처리 하시오

```
if, else
```

5) 출력된 결과가 주석과 같아지도록 하시오

```
a : lower? b : title
```

6) 변수 today에 datetime 객체가 들어있을 때 출력된 결과가 주석과 같아지도록 하시오.

```
Y년 m월 d일 (D) A h:i
```



# Form tag with Django

1) 지문의 코드 중 form 태그의 속성인 action의 역할에 대해 설명하시오. 

```
입력 데이터가 전송될 URL을 지정한다.(수신자 지정) 여기선 create/ URL로 연결시킨다.
```



2) 지문의 코드 중 method가 가질 수 있는 속성 값을 작성하시오. 

```
입력 데이터의 전달 방식을 지정하고, 가질 수 있는 속성값은 GET, POST, PUT, DELETE 등이 있다.
GET은 URL에 전달값을 노출시키며, POST는 숨긴다.
```



3) input 태그에 각각 `안녕하세요`, `반갑습니다`, `파이팅` 문자열을 넣고 submit  버튼을 눌렀을 때 이동하는 url 경로를 작성하시오

```
IP주소:포트/(app명 있다면 app명)/create/?title=안녕하세요&content=반갑습니다&my-site=파이팅
```

