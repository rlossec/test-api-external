from rest_framework.reverse import reverse

from .test_tools import ToolTestCase



class TestUpdateTool(ToolTestCase):
    def test_update_tool(self):
      url = reverse("tool-detail", args=[self.tool_1.id])
      response = self.client.put(url, self.body)
      self.assertEqual(response.status_code, 200)
      self.assertEqual(response.data["name"], "Test Create UpdateTool 1")
      self.assertEqual(response.data["website_url"], "https://test-create-update-tool-1.com")
      self.assertEqual(response.data["description"], "Test Create Update Description 1")
      self.assertEqual(response.data["owner_department"], "EN")
      self.assertEqual(response.data["vendor"], "Test Create Update Vendor 1")
      self.assertEqual(response.data["category"], self.category_1.id)