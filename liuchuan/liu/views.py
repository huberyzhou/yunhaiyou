from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Carousel
from .myser import CarouselSer
# Create your views here.


class CarouselView(APIView):
    # 获取幻灯片数据
    def get(self, request):
        pics = Carousel.objects.all()
        res = {}
        if pics:
            pic_sers = CarouselSer(pics, many=True).data
            res['code'] = 200
            res['pics'] = pic_sers
        else:
            res['code'] = 405
            res['msg'] = '未添加幻灯片'
        return Response(res)

    # 添加幻灯片
    def post(self, request):
        name = request.data.get('name')
        url = request.data.get('url')
        # 排重
        pic = Carousel.objects.filter(url=url).first()

        if pic:
            return Response({'msg': '该幻灯片已存在'})

        else:
            # 入库
            pics = Carousel(name=name, url=url)
            pics.save()
            return Response({'msg': '添加成功'})

    # 删除幻灯片
    def delete(self, request):
        pid = request.data.get('pid')
        pic = Carousel.objects.get(id=pid).delete()
        return Response({'msg': '删除成功'})
