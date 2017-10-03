from django.conf.urls import url

from articles.api.views import ArticlesListCreateAPIView, ArticleRetrieveAPIView, ArticleGetAPIView

urlpatterns = [
    url(r'^article/$', ArticleGetAPIView.as_view()),
    url(r'^articles/$', ArticlesListCreateAPIView.as_view()),
    url(r'^articles/(?P<id>[0-9]+)/$', ArticleRetrieveAPIView.as_view())
]
