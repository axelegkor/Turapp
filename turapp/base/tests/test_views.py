from django.test import TestCase, Client
from django.urls import reverse


""" class BaseTest(TestCase):
    def setUp(self):
        client = Client() """



""" class LoginTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.login_url = reverse('login')
    

    def test_user_can_access_page(self):
        response = self.client.get(self.login_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'templates/base/login.html') """