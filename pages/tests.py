from django.test import TestCase
from .models import Post
from django.urls import reverse



class PostModelTest(TestCase):
    def setUp(self):
        Post.objects.create(post = 'Hello World')
    def check_text_content(self):
        post = Post.objects.get(id=1)
        text_content = f'{post.post}'
        self.assertEqual(text_content,'Hello World')

class HomePageTest(TestCase):
    def setup(self):
        Post.objects.create(post='This is another test case')
    
    def test_url_exist(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code,200)
    
    def test_url_name(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code,200)