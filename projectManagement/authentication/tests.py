from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.home_url = reverse('authentication:home')
        self.login_url = reverse('authentication:login')
        self.logout_url = reverse('authentication:logout')
        self.signup_url = reverse('authentication:signup')
        self.check_username_url = reverse('authentication:check_username')

        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client.login(username='testuser', password='12345')

    def test_home_GET(self):
        response = self.client.get(self.home_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'authentication/home.html')

    def test_login_GET(self):
        self.client.logout()
        response = self.client.get(self.login_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'authentication/login.html')

    def test_logout_GET(self):
        response = self.client.get(self.logout_url)

        self.assertEquals(response.status_code, 302)  # Redirects to home

    def test_signup_GET(self):
        response = self.client.get(self.signup_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'authentication/sign_up.html')

    def test_check_username_POST(self):
        response = self.client.post(self.check_username_url, {'username': 'newuser'}, content_type='application/json')

        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.json(), {'available': True})