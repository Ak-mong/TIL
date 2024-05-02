from django.shortcuts import render
from django.http import JsonResponse
from django.conf import settings
from .serializers import DepositOptionsSerializer, DepositProductsSerializer
from .models import DepositOptions,DepositProducts
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import requests
from django.db.models import Max
api_key = settings.API_KEY
API_URL = 'http://finlife.fss.or.kr/finlifeapi/'
'''
다양한 API 중 정기예금 API 를 활용합니다.
• 반드시 테스트나 API 문서를 통해 전체 데이터를 눈으로 확인한 후 프로젝트를 진행합니다.
• 저장된 데이터 중 조건에 맞는 데이터를 가져오도록 구현합니다.
'''
# @api_view(['GET'])
def index(reqeust):
    url = API_URL + 'depositProductsSearch.json'
    params = {
        'auth' : api_key,
        # 금융회사 코드 020000 (은행)
        'topFinGrpNo': '020000',
        'pageNo':1
    }
    response = requests.get(url, params=params).json()
    response_data = response['result']['baseList'][0]
    response_data2 = response['result']['optionList'][0]
    context ={
        'response_data':response_data,
        'response_data2':response_data2
    }
    return JsonResponse(context)


'''
GET
requests 모듈을 활용하여 정기예금 상품 목록 데이터를 가져와 정기예금
상품 목록과 옵션 목록을 DB에 저장
'''
# @api_view(['GET'])
def save_deposit_products(request):
    # A. 정기예금 상품 목록 DB 저장
    url = API_URL + 'depositProductsSearch.json'
    params = {
        'auth' : api_key,
        # 금융회사 코드 020000 (은행)
        'topFinGrpNo': '020000',
        'pageNo':1
    }
    response = requests.get(url, params=params).json()
    for base in response.get('result').get('baseList'):
        # print('dddddddddddddddddddddddddddddddddddd',li['fin_prdt_cd'])
        
        # 원하는 데이터 추출하기
        fin_prdt_cd = base['fin_prdt_cd'] # 금융 상품 코드
        kor_co_nm = base['kor_co_nm'] # 금융회사명
        fin_prdt_nm = base['fin_prdt_nm'] # 금융 상품명
        etc_note = base['etc_note'] # 금융 상품 설명
        join_deny = base['join_deny'] # 가입 제한(1: 제한없음, 2:서민전용, 3:일부제한)
        join_member = base['join_member'] # 가입대상
        join_way = base['join_way'] # 가입 방법
        spcl_cnd = base['spcl_cnd'] # 우대조건
        # 항상 확인부터
        # print(fin_prdt_cd)
        # print(temp)
        # print(feels_like)
        product_save_data = {
            'fin_prdt_cd':fin_prdt_cd,
            'kor_co_nm':kor_co_nm,
            'fin_prdt_nm':fin_prdt_nm,
            'etc_note':etc_note,
            'join_deny':join_deny,
            'join_member':join_member,
            'join_way':join_way,
            'spcl_cnd':spcl_cnd,
        }
        # 유효성 검사
        serializer = DepositProductsSerializer(data=product_save_data)
        if serializer.is_valid(raise_exception=True):
            # 유효하다면 저장
            serializer.save()
    for option in response.get('result').get('optionList'):
        fin_prdt_cd = option['fin_prdt_cd'] # 금융 상품 코드
        intr_rate_type_nm = option['intr_rate_type_nm'] #저축금리 유형명
        intr_rate = option['intr_rate'] # 저축금리
        intr_rate2 = option['intr_rate2'] # 최고우대금리
        save_trm = option['save_trm'] 

        options_save_data ={
            'fin_prdt_cd':fin_prdt_cd,
            'intr_rate_type_nm':intr_rate_type_nm,
            'intr_rate':intr_rate,
            'intr_rate2':intr_rate2,
            'save_trm':save_trm,
        }
        # 유효성 검사
        serializer = DepositOptionsSerializer(data=options_save_data)
        if serializer.is_valid(raise_exception=True):
            product = DepositProducts.objects.get(fin_prdt_cd=options_save_data.get('fin_prdt_cd'))
            # 유효하다면 저장
            serializer.save(product=product)
    return JsonResponse({"message":"Complete Save!"})


'''
GET: 전체 정기예금 상품 목록 반환
POST: 상품 데이터 저장
'''
@api_view(['GET','POST'])
def deposit_products(request):
    # B. 전체 정기예금 상품 목록 출력
    if request.method == 'GET':
        products = DepositProducts.objects.all()
        serializer = DepositProductsSerializer(products, many=True)
        return Response(serializer.data)
    # C. 정기예금 상품 추가하기
    elif request.method == 'POST':
        serializer = DepositProductsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        error_message = {'message':'이미 있는 데이터 거나, 데이터가 잘못 입력되었습니다.'}
        return Response(error_message, status=status.HTTP_400_BAD_REQUEST)
    


'''특정 상품의 옵션 리스트 출력'''
@api_view(['GET'])
def deposit_products_options(request, fin_prdt_cd):
    # D. 특정 상품의 옵션 리스트 출력
    product = DepositProducts.objects.get(fin_prdt_cd = fin_prdt_cd)
    options = product.depositoptions_set.all()
    serializer = DepositOptionsSerializer(options, many=True)
    return Response(serializer.data)

''' 
가입 기간에 상관없이 최고 금리가 가장 높은 금융 상품과
해당 상품의 옵션 리스트 출력
'''
@api_view(['GET'])
def deposit_products_top_rate(request):
    # E. 금리가 가장 높은 상품의 정보 출력
    # product = DepositProducts.objects.filter(intr_rate2)
    # option = DepositOptions.objects.get(intr_rate2 = DepositOptions.objects.aggregate(intr_rate2=Max('intr_rate2'))['intr_rate2'])
    max_rate = DepositOptions.objects.aggregate(max_rate=Max('intr_rate2'))['max_rate']
    # 가장 높은 금리를 가진 상품의 옵션을 가져옵니다.
    options = DepositOptions.objects.filter(intr_rate2=max_rate)
    print(options)
    products = [option.product for option in options]
    print(products)
    # serializer = DepositProductsSerializer(products, many=True)
    product_serializer = DepositProductsSerializer(products, many=True)
    options_serializer = DepositOptionsSerializer(options, many=True)
    # print('----------------------',product_serializer)
    # print('----------------------',options_serializer)
    context ={
        'deposit_product':product_serializer.data,
        'options':options_serializer.data
    }
    return Response(context)