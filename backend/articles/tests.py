from rest_framework import status
from rest_framework.test import APITestCase

from articles.models import Article


class ArticlesListCreateAPITest(APITestCase):

    def setUp(self):
        Article.objects.create(
            title="Title 1", text="Text 1"
        )
        Article.objects.create(
            title="Title 2", text="Text 2"
        )

    def test_get_articles_list(self):

        response = self.client.get('/articles/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, [
            {
                'title': "Title 2",
                'text': "Text 2"
            },
            {
                'title': "Title 1",
                'text': "Text 1"
            }
        ])

    def test_create_article(self):

        response = self.client.post(
            '/articles/',
            data={
                'title': "Title 3",
                'text': "Text 3",
            }
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data, {
            'title': "Title 3",
            'text': "Text 3"
        })


class ArticleRetrieveAPITest(APITestCase):

    def setUp(self):
        self.article = Article.objects.create(
            title="Title 1", text="Text 1"
        )
        Article.objects.create(
            title="Title 2", text="Text 2"
        )

    def test_retrieve_article(self):

        response = self.client.get(
            '/articles/{id}/'.format(id=self.article.id)
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {
            'title': "Title 1",
            'text': "Text 1"
        })

    def test_retrieve_not_existing_article(self):

        response = self.client.get('/articles/0/')

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class ArticleGetAPITest(APITestCase):

    def test_get_article(self):

        response = self.client.get('/article/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(set(response.data.keys()), {
            'author', 'title', 'description', 'url', 'urlToImage', 'publishedAt'
        })
