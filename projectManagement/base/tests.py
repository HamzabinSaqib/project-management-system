import time
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Project

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.home_url = reverse('base:home')
        self.new_project_url = reverse('base:new_Project')

        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client.login(username='testuser', password='12345')

        self.project = Project.objects.create(
            manager=self.user,
            projName='Test Project',
            projDesc='Test Project Description',
            projStatus='In Progress',
        )
        
        self.project_url = reverse('base:project', args=[str(self.project.projID)])
        self.delete_project_url = reverse('base:del_project', args=[str(self.project.projID)])

    def test_home_GET(self):
        start_time = time.time()
        response = self.client.get(self.home_url)
        end_time = time.time()
        
        response_time = end_time - start_time
        print(f"Home GET response time: {response_time} seconds")

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'base/home.html')

    def test_project_GET(self):
        start_time = time.time()
        response = self.client.get(self.project_url)
        end_time = time.time()
        
        response_time = end_time - start_time
        print(f"Project GET response time: {response_time} seconds")

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'base/project.html')

    def test_new_project_GET(self):
        start_time = time.time()
        response = self.client.get(self.new_project_url)
        end_time = time.time()
        
        response_time = end_time - start_time
        print(f"New Project GET response time: {response_time} seconds")

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'base/project_creation.html')

    def test_delete_project_POST(self):
        start_time = time.time()
        response = self.client.post(self.delete_project_url)
        end_time = time.time()
        
        response_time = end_time - start_time
        print(f"Delete Project POST response time: {response_time} seconds")

        self.assertEquals(response.status_code, 302)  # Redirects to home