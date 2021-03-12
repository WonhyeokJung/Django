# 1. Model 반영하기

**"Django가 Model에 생긴 변화를 DB에 반영하는 방법”을 뜻하는 용어를 작성하시오.**

```
Migrations
```



# 2.Model 변경사항 저장하기

```python
class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
```



**위에서 작성한 Model의 변경 사항을 저장하기 위한 명령어를 작성하시오. 이로 인해 생성 된 파일에 대응되는 SQL문을 확인하는 명령어와 출력 결과를 작성하시오.**

```
저장 명령어 : save()
저장 후 생성된 파일에 대응하는 SQL문을 확인하는 명령어
Article.objects.all() # 전부 출력
결과 : <QuerySet [<Article: Article object(n)>]..>

Article.objects.get(pk=n)
결과 : <Article:Article object ()> # 단 하나만 출력가능. 2개 이상 존재시 에러. 따라서 pk사용

Article.objects.filter(title="")
결과 : <QuerySet> # 여러 개도 출력가능. 단 하나라도 QuerySet으로 출력한다.
```



# 3.Python Shell

**Django에서 사용 가능한 모듈 및 메서드를 대화식 Python Shell에서 사용하려고 할 때, 어 떠한 명령어를 통해 해당 Shell을 실행할 수 있는지 작성하시오.**

```
python manage.py shell
```



# 4. Django Model Field

**Django에서 Model을 정의할 때 사용할 수 있는 필드 타입을 5가지 이상 작성하시오**

```python
DateTimeField(), CharField(), TextField(), IntegerField(), TimeField(), FileField()...
```

