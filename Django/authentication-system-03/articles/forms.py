from django import forms
from .models import Article,Comment


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__'

# aritcles/forms.py
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)