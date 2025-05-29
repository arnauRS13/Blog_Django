from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from .models import Author, Post, Tag
from django.utils import timezone
from django.urls import reverse

class BlogModelTests(TestCase):

    def setUp(self):
        # Crear autor
        self.author = Author.objects.create(
            first_name="Arnau", last_name="Rodriguez", email="arnau@test.com"
        )

        # Crear tags
        self.tag1 = Tag.objects.create(tag="esport")
        self.tag2 = Tag.objects.create(tag="noticies")

        # Crear post
        self.post = Post.objects.create(
            title="Post de prova",
            excerpt="Resum de prova",
            image_name="prova.jpg",
            date=timezone.now().date(),
            slug="post-de-prova",
            content="Contingut complet",
            author=self.author
        )
        self.post.tags.set([self.tag1, self.tag2])

    def test_author_str(self):
        self.assertEqual(str(self.author), "Arnau Rodriguez")

    def test_tag_str(self):
        self.assertEqual(str(self.tag1), "esport")

    def test_post_str(self):
        self.assertEqual(str(self.post), "Post de prova")

    def test_post_author_relation(self):
        self.assertEqual(self.post.author.email, "arnau@test.com")

    def test_post_tags_relation(self):
        tags = self.post.tags.all()
        self.assertIn(self.tag1, tags)
        self.assertIn(self.tag2, tags)


class BlogViewTests(TestCase):

    def setUp(self):
        self.author = Author.objects.create(first_name="Test", last_name="Autor", email="test@ex.com")
        self.tag = Tag.objects.create(tag="testtag")
        self.post = Post.objects.create(
            title="Test Post",
            excerpt="Resum",
            image_name="test.jpg",
            date=timezone.now().date(),
            slug="test-post",
            content="Contingut llarg",
            author=self.author
        )
        self.post.tags.add(self.tag)

    def test_index_view(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Post")

    def test_post_list_view(self):
        response = self.client.get(reverse('post-list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Post")

    def test_post_detail_view(self):
        response = self.client.get(reverse('posts-detail-page', args=["test-post"]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Contingut llarg")

    def test_authors_list_view(self):
        response = self.client.get(reverse('authors-list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Autor")

    def test_author_detail_view(self):
        response = self.client.get(reverse('author-detail', args=[self.author.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Autor")

    def test_tags_list_view(self):
        response = self.client.get(reverse('tags-list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "testtag")

    def test_tag_post_list_view(self):
        response = self.client.get(reverse('tag-post-list', args=["testtag"]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Post")