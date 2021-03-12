# 1. MTV

**Django는 MTV 디자인 패턴으로 이루어진 Web Framework이다. 여기서 MTV는 무엇의 약자이며 각각 MVC 디자인 패턴과 어떻게 매칭이 되며 각 키워드가 django에서 하는 역할을 간략히 서술하시오.**

```
MTV란, Model, Template, View의 약자이며,
각각 MVC의 Model, View, Controller와 대응된다.

M : DB 관리
T : Layout(화면, UI)
V : 중심 컨트롤러(제어)
의 역할을 한다.
```



# 2. URL

**__(a)__는 Django에서 URL 자체를 변수처럼 사용해서 동적으로 주소를 만드는 것을 의미한다. __(a)__는 무엇인지 작성하시오.**



```
Variable Routing
```



# 3. Django Template Path

**Django 프로젝트는 render할 template 파일들을 찾을 때, 기본적으로 settings.py에 등록된 각 앱 폴더 안의 __(a)__ 폴더 내부를 탐색한다. __(a)__에 들어갈 폴더 이름을 작성하시오.**



```python
Templates.
Templates 폴더를 settings.py INSTALLED_APPS에 등록된 순서대로 탐색
따라서 같은 이름의 html 파일 존재시 순서에 따라 다른 HTML 파일을 불러올 가능성이 존재한다.
```



# 4. Static web and Dynamic web

```
Static web page : 정적 웹 페이지. 미리 저장된 파일이 요청에 따라 그대로 전달된다. 고정된 웹페이지
Dynamic web page : 동적 웹 페이지. 데이터를 가공하여 상황, 시간, 요청에 따라 다른 반응형 웹페이지.
```

