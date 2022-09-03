from django.db import models

# Create your models here.
# 1. 모델 클래스 생성 및 models.Model 상속 << 상속을 해야 db에서 사용이 가능
class Article(models.Model):
    # title -> char
    title = models.CharField(max_length=10)
    # content -> text
    content = models.TextField()
    # created_at -> Datetime
    created_at = models.DateTimeField(auto_now_add=True)
    # updated_at -> Datetime
    updated_at = models.DateTimeField(auto_now=True)