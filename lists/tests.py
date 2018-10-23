from django.http import HttpRequest
from django.test import TestCase
# Create your tests here.
from django.urls import resolve

from lists.views import home_page


class SmokeTest(TestCase):
    def test_bad_maths(self):
        self.assertEqual(1 + 2, 3)


class HomePageTest(TestCase):
    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_return_correct_html1(self):
        request = HttpRequest()
        response = home_page(request)
        html = response.content.decode('UTF-8')
        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<title>To-Do lists</title>', html)
        self.assertTrue(html.strip().endswith('</html>'))

    def test_home_page_return_correct_html2(self):
        response = self.client.get('/')
        html = response.content.decode('UTF-8')
        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<title>To-Do lists</title>', html)
        self.assertTrue(html.strip().endswith('</html>'))
        self.assertTemplateUsed(response, 'home.html')

    def test_uses_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

    def test_can_save_a_POST_request(self):
        response = self.client.post('/', data={'item_text': 'A new list item'})
        self.assertIn('A new list item', response.content.decode())
        self.assertTemplateUsed(response, 'home.html')
