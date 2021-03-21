from django.db import models

# Create your models here.
class Article(models.Model):
    # ORM은 models.py 내부의 class에서, Class variable만 확인하여 DB의 Column으로 만든다.
    title = models.CharField(max_length=100)
    content = models.TextField()
    # email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.id} => {self.title}'
    
