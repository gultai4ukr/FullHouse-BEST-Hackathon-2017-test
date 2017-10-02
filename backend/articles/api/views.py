from rest_framework import generics
from rest_framework.permissions import AllowAny

from articles.api.serializers import ArticleSerializer
from articles.models import Article


class ArticlesListCreateAPIView(generics.ListCreateAPIView):
    permission_classes = (AllowAny, )
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()


class ArticleRetrieveAPIView(generics.RetrieveAPIView):
    permission_classes = (AllowAny, )
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()
    lookup_field = 'id'
