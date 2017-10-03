from rest_framework import status
from rest_framework.test import APITestCase

from articles.api.views import ArticleGetAPIView


class ArticleGetAPITest(APITestCase):

    def test_get_article(self):

        response = self.client.get('/article/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(set(response.data.keys()), {
            'author', 'title', 'description', 'url', 'urlToImage', 'publishedAt', 'source'
        })

    def test_get_article_by_category(self):

        response = self.client.get(
            '/article/?category=business'
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(set(response.data.keys()), {
            'author', 'title', 'description', 'url', 'urlToImage', 'publishedAt', 'source'
        })
        self.assertIn(response.data['source'], ArticleGetAPIView.SOURCES_BY_CATEGORY['business'])

    def test_get_article_by_language(self):

        response = self.client.get(
            '/article/?language=en'
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(set(response.data.keys()), {
            'author', 'title', 'description', 'url', 'urlToImage', 'publishedAt', 'source'
        })
        self.assertIn(response.data['source'], ArticleGetAPIView.SOURCES_BY_LANGUAGE['en'])

    def test_get_article_by_country(self):

        response = self.client.get(
            '/article/?country=us'
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(set(response.data.keys()), {
            'author', 'title', 'description', 'url', 'urlToImage', 'publishedAt', 'source'
        })
        self.assertIn(response.data['source'], ArticleGetAPIView.SOURCES_BY_COUNTRY['us'])
