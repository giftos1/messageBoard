from django.test import TestCase
from django.urls import reverse

from posts.models import Post


# Create your tests here.
class PostModelTest(TestCase):
    def setUp(self):
        Post.objects.create(text='test post')  # create new database entry

    def test_text_content(self):
        post = Post.objects.get(id=1)  # Django predefines ids for each line in database
        expected_object_name = f'{post.text}'
        self.assertEqual(expected_object_name, 'test post')


class HomePageViewTest(TestCase):

    def setUp(self):
        Post.objects.create(text='another test')

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_by_name(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'home.html')
