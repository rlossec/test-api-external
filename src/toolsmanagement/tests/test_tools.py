# python manage.py test toolsmanagement.tests.test_tools
from datetime import datetime
from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase
from rest_framework.reverse import reverse

from toolsmanagement.models import Tool, Category


User = get_user_model()

class ToolTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser",
                                             email="testuser@test.com",
                                             hire_date=datetime.now(),
                                             is_active=True)
        
        self.client.force_authenticate(user=self.user)

        self.category_1 = Category.objects.create(name="Test Category 1")
        self.category_2 = Category.objects.create(name="Test Category 2")
        self.tool_1 = Tool.objects.create(name="Test Tool 1", 
                                          website_url="https://test-tool-1.com", 
                                          description="Test Description", 
                                          owner_department="EN", 
                                          vendor="Test Vendor",
                                          category=self.category_1,
                                          base_monthly_cost=100)
        self.tool_2 = Tool.objects.create(name="Test Tool 2",
                                          website_url="https://test-tool-2.com",
                                          description="Test Description 2",
                                          owner_department="SA",
                                          vendor="Test Vendor 2",
                                          category=self.category_2,
                                          base_monthly_cost=200)
        self.body = {
            "name": "Test Create UpdateTool 1",
            "website_url": "https://test-create-update-tool-1.com",
            "description": "Test Create Update Description 1",
            "owner_department": "EN",
            "vendor": "Test Create Update Vendor 1",
            "category": self.category_1.id,
            "base_monthly_cost": 100}

    def test_list_tools(self):
        url = reverse("tool-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]["name"], "Test Tool 1")
        self.assertEqual(response.data[1]["name"], "Test Tool 2")

    def test_create_tool(self):
        url = reverse("tool-list")
        response = self.client.post(url, self.body)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data["name"], "Test Create UpdateTool 1")
        self.assertEqual(response.data["website_url"], "https://test-create-update-tool-1.com")
        self.assertEqual(response.data["description"], "Test Create Update Description 1")
        self.assertEqual(response.data["owner_department"], "EN")
        self.assertEqual(response.data["vendor"], "Test Create Update Vendor 1")
        self.assertEqual(response.data["category"], self.category_1.id)
        self.assertEqual(response.data["base_monthly_cost"], 100.00)