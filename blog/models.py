from django.db import models


# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=30)  # 제목은 30자 까지 지정
    content = models.TextField()

    # created_at = models.DateTimeField()  #수정 전 코드
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # author : 추후 작성 예정

    def __str__(self):
        return f'[{self.pk}] {self.title}'
    def get_absolute_url(self):
        return f'/blog/{self.pk}/'