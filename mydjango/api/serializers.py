#Serializer는 장고 모델 데이터를 json 타입으로 바꿔주는 작업을 해줌
#즉, 직렬화 작업 json 데이터 형태로 api 호출에 응답하기 위해서

from rest_framework import serializers
from .models import Item

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ("__all__")
        #fields = ('name', 'description', 'cost')