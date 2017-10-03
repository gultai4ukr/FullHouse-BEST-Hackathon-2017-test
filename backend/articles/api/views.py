import random

import requests
from django.conf import settings
from rest_framework import generics
from rest_framework import status
from rest_framework import views
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

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


class ArticleGetAPIView(views.APIView):

    SOURCES_URL = 'https://newsapi.org/v1/sources'
    ARTICLES_URL = 'https://newsapi.org/v1/articles'

    CATEGORIES = [
        'business', 'entertainment', 'gaming', 'general', 'music',
        'politics', 'science-and-nature', 'sport', 'technology'
    ]

    SOURCES = [
        'abc-news-au', 'al-jazeera-english', 'ars-technica', 'associated-press', 'bbc-news', 'bbc-sport',
        'bild', 'bloomberg', 'breitbart-news', 'business-insider', 'business-insider-uk', 'buzzfeed',
        'cnbc', 'cnn', 'daily-mail', 'der-tagesspiegel', 'die-zeit', 'engadget', 'entertainment-weekly',
        'espn', 'espn-cric-info', 'financial-times', 'focus', 'football-italia', 'fortune', 'four-four-two',
        'fox-sports', 'google-news', 'gruenderszene', 'hacker-news', 'handelsblatt', 'ign', 'independent',
        'mashable', 'metro', 'mirror', 'mtv-news', 'mtv-news-uk', 'national-geographic', 'new-scientist',
        'newsweek', 'new-york-magazine', 'nfl-news', 'polygon', 'recode', 'reddit-r-all', 'reuters',
        'spiegel-online', 't3n', 'talksport', 'techcrunch', 'techradar', 'the-economist', 'the-guardian-au',
        'the-guardian-uk', 'the-hindu', 'the-huffington-post', 'the-lad-bible', 'the-new-york-times',
        'the-next-web', 'the-sport-bible', 'the-telegraph', 'the-times-of-india', 'the-verge',
        'the-wall-street-journal', 'the-washington-post', 'time', 'usa-today', 'wired-de', 'wirtschafts-woche'
    ]

    SOURCES_BY_CATEGORY = {
        'general': [
            'abc-news-au', 'al-jazeera-english', 'associated-press', 'bbc-news', 'bild', 'cnn',
            'der-tagesspiegel', 'focus', 'google-news', 'independent', 'metro', 'mirror', 'newsweek',
            'new-york-magazine', 'reddit-r-all', 'reuters', 'spiegel-online', 'the-guardian-au',
            'the-guardian-uk', 'the-hindu', 'the-huffington-post', 'the-new-york-times', 'the-telegraph',
            'the-times-of-india', 'the-washington-post', 'time', 'usa-today'
        ],
        'politics': ['breitbart-news'],
        'music': ['mtv-news', 'mtv-news-uk'],
        'entertainment': ['buzzfeed', 'daily-mail', 'entertainment-weekly', 'mashable', 'the-lad-bible'],
        'technology': [
            'ars-technica', 'engadget', 'gruenderszene', 'hacker-news', 'recode',
            't3n', 'techcrunch', 'techradar', 'the-next-web', 'the-verge', 'wired-de'
        ],
        'science-and-nature': ['national-geographic', 'new-scientist'],
        'sport': [
            'bbc-sport', 'espn', 'espn-cric-info', 'football-italia', 'four-four-two',
            'fox-sports', 'nfl-news', 'talksport', 'the-sport-bible'
        ],
        'gaming': ['ign', 'polygon'],
        'business': [
            'bloomberg', 'business-insider', 'business-insider-uk', 'cnbc', 'die-zeit', 'financial-times',
            'fortune', 'handelsblatt', 'the-economist', 'the-wall-street-journal', 'wirtschafts-woche'
        ]
    }

    def get(self, request, *args, **kwargs):
        category = request.query_params.get('category')

        if category and category in self.CATEGORIES:
            source = random.choice(self.SOURCES_BY_CATEGORY[category])
        else:
            source = random.choice(self.SOURCES)

        response = requests.get(
            '{base_url}?source={source}&apiKey={api_key}'.format(
                base_url=self.ARTICLES_URL, source=source, api_key=settings.NEWS_API_KEY
            )
        )
        json = response.json()

        if response.ok and json['status'] == 'ok':
            article = random.choice(json['articles'])
            return Response(article)
        else:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
