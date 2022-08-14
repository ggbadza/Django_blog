from django.db import models

# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=30)
    content=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'[{self.pk}]{self.title}' #f-스트링. {} 안에 변수 값을 출력

    def get_detail_url(self):
        return f'/blog/{self.pk}'