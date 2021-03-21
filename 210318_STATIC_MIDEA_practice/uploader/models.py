from django.db import models
from imagekit.models import ProcessedImageField
# from imagekit import models 이름 겹치면 아래가 이겨서 models겹치므로 금지
from imagekit.processors import Thumbnail

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    # 이미지 업로드 안해도 ㄱㅊ다.(blank여도 okay)
    # ORM이 빈 것을 허용함. DB는 자동으로 ''(빈 문자열)이 저장됨.
    # 비어있을떄, is_valid() 통과. 유효한 것으로 판단.
    # image = models.ImageField(blank=True) 내장

    # 이미지 리사이징. 서버에 그렇게 큰 이미지들 다 받아줄수 없음
    image = ProcessedImageField(
        upload_to='article/',  # UPLOAD할 폴더 지정
        blank=True,
        # 근데 이렇게 하면 잘림. 사진 크기를 resizing하는 옵션을 따로 써야함.
        # detail은 크게, 목록에선 작게도 가능함.
        processors=[Thumbnail(200, 300)],
        format='JPEG',
        options={'quality': 90}, # 90퍼 정도로 퀄리티 낮추겠다.
    )
    # file = models.FileField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)