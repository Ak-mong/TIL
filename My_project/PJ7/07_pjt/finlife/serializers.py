from rest_framework import serializers
from .models import DepositOptions,DepositProducts

class DepositOptionsSerializer(serializers.ModelSerializer):
    '''
    DepositOptions 모델 사용
    모든 필드를 사용하도록 설정
    '''
    class Meta:
        model = DepositOptions
        read_only_fields = ('product',)
        fields = '__all__'

class DepositProductsSerializer(serializers.ModelSerializer):
    '''
    DepositProducts 모델 사용
    외래키로 설정된 product 필드는 읽기전용으로 설정
    모든 필드를 사용하도록 설정
    '''
    # class ProductOptionsSerializer(serializers.ModelSerializer):
    #     class Meta:
    #         model = DepositOptions
    #         fields = '__all__'
    #         # read_only_fields = ('product',)
            
    # depositoptions_set = ProductOptionsSerializer(read_only=True, many=True)
    class Meta:
        model = DepositProducts
        fields = '__all__'

