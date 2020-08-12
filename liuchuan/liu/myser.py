# 导包
from rest_framework import serializers
from liu.models import Carousel


# 幻灯片序列器
class CarouselSer(serializers.ModelSerializer):
    class Meta:
        model = Carousel
        fields = '__all__'
