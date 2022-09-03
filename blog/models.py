from django.db import models
import os

# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=30)
    content=models.TextField()
    head_image = models.ImageField(upload_to='blog/images/%Y_%m_%d/', blank=True) #폴더 여러개로 구분시켜야지 성능 영향 X, blank는 비어도 된다는 뜻
    upload_file = models.FileField(upload_to='blog/files/%Y_%m_%d/', blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'[{self.pk}]{self.title}' #f-스트링. {} 안에 변수 값을 출력

    def get_detail_url(self):
        return f'/blog/{self.pk}'

    def file_name(self):
        return os.path.basename(self.upload_file.name)