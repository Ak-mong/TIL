from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .models import Article
from .serializers import ArticleListSerializer, ArticleSerializer

@api_view(['GET','POST'])
def article_list(request):
    if request.method == "GET":
        articles = Article.objects.all()
        serializer = ArticleListSerializer(articles, many=True) # 단일 데이터가 아니기 때문
        '''
        context = {
            'articles':articles
        }
        '''
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
        

@api_view(['GET','DELETE','PUT'])
def article_detail(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'PUT':
        serializer = ArticleSerializer(article, data=request.data, partial=True)
        # serializer = ArticleSerializer(instance = article, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)    
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)