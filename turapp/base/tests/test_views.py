from django.test import TestCase, Client
from django.urls import reverse



class AccessTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.login_url = reverse('login')
        self.register_url = reverse('register')
    

    def test_user_can_access_loginPage(self):
        response = self.client.get(self.login_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'base/login.html')

    def test_user_can_access_registerPage(self):
        response = self.client.get(self.register_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'base/register.html')