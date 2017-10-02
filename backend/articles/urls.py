from django.conf.urls import url

from articles.api.views import ArticlesListCreateAPIView, ArticleRetrieveAPIView

urlpatterns = [
    url(r'^$', ArticlesListCreateAPIView.as_view()),
    url(r'^(?P<id>[0-9]+)/$', ArticleRetrieveAPIView.as_view()),
]
