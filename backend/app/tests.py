from django.test import TestCase
from django.contrib.auth.models import User
from .models import *

class BlogModelTest(TestCase):
    def setUp(self):
        # Create a user for testing
        self.user = User.objects.create_user(username='testuser', password='testpassword')

    def test_blog_creation(self):
        blog = Blog.objects.create(
            title='Test Blog',
            category_name='Test Category',
            description='This is a test blog post.',
            author=self.user,
            views_count=4,
            images=None
        )
        self.assertEqual(blog.title, 'Test Blog')
        self.assertEqual(blog.category_name, 'Test Category')
        self.assertEqual(blog.description, 'This is a test blog post.')
        self.assertEqual(blog.author, self.user)
        self.assertEqual(blog.views_count, 0)
        self.assertIsNone(blog.images)

    def test_blog_str_method(self):
        blog = Blog.objects.create(
            title='Test Blog',
            category_name='Test Category',
            description='This is a test blog post.',
            author=self.user,
            views_count=0,
            images=None
        )
        self.assertEqual(str(blog), 'Test Blog')

