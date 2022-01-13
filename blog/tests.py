from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from .models import Post
# Create your tests here.


class BlogTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create(
            username='yoofi', email='test@gmail.com', password='secret')

        self.post = Post.objects.create(
            title='Test Post', body='Test body', author=self.user)

    def test_string_representation(self):
        post = Post(title="This is a test")
        self.assertEqual(post.title, str(post))

    def test_post_content(self):
        self.assertEqual(f'{self.post.title}', 'Test Post')
        self.assertEqual(f'{self.post.body}', 'Test body')
        self.assertEqual(f'{self.post.author}', 'yoofi')

    def test_post_list_view(self):
        resp = self.client.get(reverse('blog:index'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'blog/index.html')

    def test_post_detail_view(self):
        resp = self.client.get('/blog/post/1/')
        self.assertEqual(resp.status_code, 200)
        no_resp = self.client.get('/blog/post/50/')
        self.assertEqual(no_resp.status_code, 404)
