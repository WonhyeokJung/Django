from django.shortcuts import render, redirect, get_object_or_404  # redirect 임포트 / 에러 발생시 404페이지
from .models import Student  # 데이터베이스 담당자 models.py import

# Create(생성)
def new(request):
    return render(request, 'orm_practice/new.html')

def create(request):
    # 자료 받으면 받아서 다 저장
    if request.method == 'POST':
        student = Student()
        student.name = request.POST.get('name')  # request에서 자료 GET하여, name = name인것을 받아온다.
        student.age = request.POST.get('age')
        student.major = request.POST.get('major')
        student.intro = request.POST.get('intro')
        student.created_at = request.POST.get('created_at')
        student.updated_at = request.POST.get('updated_at')
        student.save()
        # return redirect('index')  # 다시 다른 곳으로 보냄. urls의 name='index'로
        return redirect('appname:detail', pk=student.pk)  # detail은 pk인자 하나가 필요함 detail/pk구조
        # appname:detail인걸 보면, urls의 name값 참조해서 불러옴. redirect의 특징
    elif request.method == 'GET':
        return redirect('/practice/new/') # 지멋대로 오면, 여기 거쳐서 오게 되돌려보냄. 하드코딩방식


# Retrieve / Read (조회)
# 여러개 조회
def index(request):
    # DB인스턴스는 Class의 복수형
    students = Student.objects.all()
    # context는 아주 간결하게. 코드는 위에 다 작성
    context = {
        'students':students,
    }
    return render(request, 'orm_practice/index.html', context)

# 단일조회
def detail(request, pk):
    student = get_object_or_404(Student, pk=pk) # 클래스명, 변수들
    # student = Student.objects.get(pk=pk)  # detail의 pk와 get pk는 다른것임.
    context ={
        'student' : student,
    }
    return render(request, 'orm_practice/detail.html', context)


# Update
## 수정용 HTML 제공
def edit(request, pk):
    student = Student.objects.get(pk=pk)  # edit에서 student.id등 사용이 가능해짐
    context = {
        'student':student
    }
    return render(request, 'orm_practice/edit.html', context)

## 실제 수정
def update(selfs, pk):
    if selfs.method == 'POST':
        student = Student.objects.get(pk=pk)  # create와 기존에 있는 거 찾는것만 다름
        # 굳이 실제 수정과 다른지 if로 체크할 필요없음 더 귀찮아짐
        student.name = selfs.POST['name']  # request에서 자료 GET하여, name = name인것을 받아온다.
        student.age = selfs.POST.get('age')
        student.major = selfs.POST.get('major')
        student.intro = selfs.POST.get('intro')
        student.created_at = selfs.POST.get('created_at')
        student.updated_at = selfs.POST.get('updated_at')
        student.save()
        return redirect('appname:detail', pk=student.pk)
    return redirect('appname:edit', pk=pk) # 지멋대로 주소쳐서 들어오면 GET으로 오므로 redirect시킴


# Delete
# Detail주소에서 /delete하면 지워짐 [내가 설정한 주소상]
def delete(request, pk):
    if request.method == 'POST':
        student = Student.objects.get(pk=pk)
        student.delete()
        return redirect('appname:index')
    return redirect('appname:detail', pk=pk)  # 너도 멋대로 주소쳐서 들어왔으면 detail페이지로 보낸다.
