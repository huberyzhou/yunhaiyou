from django.db import models

# Create your models here.


class Carousel(models.Model):
    # 名称
    name = models.CharField(max_length=100, default='')
    # 路由
    url = models.CharField(max_length=120, default='')

    class Meta:
        db_table = 'carousel'
