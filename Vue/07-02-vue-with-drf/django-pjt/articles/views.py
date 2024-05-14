from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

# permission Decorators
from rest_framework.decorators import permission_classes # 주석이었던 것
from rest_framework.permissions import IsAuthenticated, IsAdminUser # 주석이었던 것

from django.shortcuts import get_object_or_404, get_list_or_404

from .serializers import ArticleListSerializer, ArticleSerializer
from .models import Article


@api_view(['GET', 'POST'])
# 전역설정을 받지만? 데코레이터가 덮어 씌운다.
# @permission_classes([IsAdminUser]) # 동작 테스트를 위해 잠시 추가, admin 유저일때만 사용 가능하도록 허용
@permission_classes([IsAuthenticated]) # 주석이었던 것, 인증된 사용자만 쓸 수 있다.
def article_list(request):
    if request.method == 'GET':
        articles = get_list_or_404(Article)
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            # serializer.save()
            serializer.save(user=request.user) # 주석이었던 것
            return Response(serializer.data, status=status.HTTP_201_CREATED)

# 이건 전역 설정을 받는다.
@api_view(['GET'])
def article_detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)

    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        print(serializer.data)
        return Response(serializer.data)
