from django.db import models


class RecipesInfo(models.Model):
    id = models.PositiveIntegerField('ID', primary_key=True)
    title = models.CharField('料理名', max_length=100)
    making_time = models.CharField('作成時間', max_length=100)
    serves = models.CharField('人数', max_length=100)
    ingredients = models.CharField('材料', max_length=1000)
    cost = models.CharField('コスト', max_length=100)
    created_at = models.DateTimeField(verbose_name='作成日時', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='更新日時', auto_now_add=True)
