from django.test import TestCase
from rest_framework.test import APITestCase
from django.urls import reverse 
from rest_framework  import status
from .models import Category

# Create your tests here.
class APITests(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.category = Category.objects.create(
            name = 'test',
            url = '#'
        )
    
    def test_api_category_list(self):
        response = self.client.get(reverse('blog:api_v1:category'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Category.objects.count(), 1)
        self.assertContains(response, self.category)