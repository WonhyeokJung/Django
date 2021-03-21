from django.db import models

# Create your models here.
class Reservation(models.Model):
    name = models.CharField(max_length=10)
    number = models.IntegerField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        # 여기 그룹으로 보내는 법.
        board_menu = [ self.name, self.number ]
        return self.number
    
