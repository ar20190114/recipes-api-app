from django.db import models
from uuid import uuid4


class RecipesInfo(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, unique=True)
    title = models.CharField('料理名', max_length=100)
    making_time = models.CharField('作成時間', max_length=100)
    serves = models.CharField('人数', max_length=100)
    ingredients = models.CharField('材料', max_length=1000)
    cost = models.CharField('コスト', max_length=100)
    created_at = models.DateTimeField(verbose_name='作成日時', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='更新日時', auto_now_add=True)
