from django.test import TestCase
from .models import Post
from django.urls import reverse

class PostModelTest(TestCase):
    def setUp(self) -> None:
        Post.objects.create(text="testing the model")

    def test_context(self):
        post = Post.objects.get(id=1)
        expected_name = f'{post.text}'
        self.assertEqual(expected_name, 'testing the model')


class HomeViewTest(TestCase):
    def setUp(self) -> None:
        Post.objects.create(text="another test")

    def test_url_location(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_url_name(self):
        response =self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_correct_template(self):
        response =self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')