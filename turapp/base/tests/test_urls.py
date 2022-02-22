from django.test import SimpleTestCase
from django.urls import reverse, resolve
from base.views import loginPage, logoutUser, enrolled, overview, mypage, description, home, about


class TestUrls(SimpleTestCase):

    def test_login_url_resolves(self):
        url = reverse('login')
        self.assertEquals(resolve(url).func, loginPage)

    
    def test_logout_url_resolves(self):
        url = reverse('logout')
        self.assertEquals(resolve(url).func, logoutUser)

    
    def test_mypage_url_resolves(self):
        url = reverse('mypage')
        self.assertEquals(resolve(url).func, mypage)


    def test_description_url_resolves(self):
        url = reverse('description')
        self.assertEquals(resolve(url).func, description)


    def test_overview_url_resolves(self):
        url = reverse('overview')
        self.assertEquals(resolve(url).func, overview)


    def test_enrolled_url_resolves(self):
        url = reverse('enrolled')
        self.assertEquals(resolve(url).func, enrolled)


    def test_about_url_resolves(self):
        url = reverse('about')
        self.assertEquals(resolve(url).func, about)


    def test_home_url_resolves(self):
        url = reverse('home')
        self.assertEquals(resolve(url).func, home)

