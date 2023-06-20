from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ItemSerializer
from .models import Item

#ModelViewSet은 기본적으로 CRUD를 지원
#Viewset의 장점
#queryset 사용으로 반복되는 CRUD 로직을 한번에 정의
#Router를 사용함으로써, URL 설정을 다룰 필요 X

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer #serializer에서 정의한 ItemSerializer를 사용