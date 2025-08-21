from rest_framework.reverse import reverse

from .test_tools import ToolTestCase


class TestCreateTool(ToolTestCase):

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
    
