from rest_framework import serializers
from .models import Article, Comment


class ArticleListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = ('id', 'title', 'content',)


class ArticleSerializer(serializers.ModelSerializer):

    class CommentDetailSerializer(serializers.ModelSerializer):
        class Meta:
            model = Comment
            fields = ('id','content',)
            # read_only_fields = ('article',)

    # 필드상으로 존재하지 않기때문에 직접 추가해줘야함
    comment_set = CommentDetailSerializer(read_only=True, many=True)
    
    # 필드 상에도 존재하지 않고, 실제로도 없어서 이름이 정해져있지 않음 => 새로운 필드
    comment_count = serializers.IntegerField(source='comment_set.count', read_only = True)

    class Meta:
        model = Article
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class ArticleTitleSerializer(serializers.ModelSerializer):
        class Meta:
            model = Article
            fields = ('title',)

    article = ArticleTitleSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = '__all__'
        # read_only_fields = ('article',)
