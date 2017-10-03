from django.conf.urls import url

from articles.api.views import ArticleGetAPIView

urlpatterns = [
    url(r'^article/$', ArticleGetAPIView.as_view())
]
