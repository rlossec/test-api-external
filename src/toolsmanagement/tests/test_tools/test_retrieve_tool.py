from rest_framework.reverse import reverse

from .test_tools import ToolTestCase


class TestRetrieveTool(ToolTestCase):
    
    def test_retrieve_tool(self):
      url = reverse("tool-detail", args=[self.tool_1.id])
      response = self.client.get(url)
      self.assertEqual(response.status_code, 200)
      self.assertEqual(response.data["name"], "Test Tool 1")
      self.assertEqual(response.data["website_url"], "https://test-tool-1.com")
      self.assertEqual(response.data["description"], "Test Description")
      self.assertEqual(response.data["owner_department"], "Engineering")
      self.assertEqual(response.data["vendor"], "Test Vendor")
      self.assertEqual(response.data["category"], self.category_1.name)
      # Shoudld include "usage_metrics" field with this structure :  "usage_metrics": {
      # "last_30_days": {
      #   "total_sessions": 127,
      #   "avg_session_minutes": 45
      # }
      # }
      self.assertIn("usage_metrics", response.data)
      self.assertIn("last_30_days", response.data["usage_metrics"])
      self.assertIn("total_sessions", response.data["usage_metrics"]["last_30_days"])
      self.assertIn("avg_session_minutes", response.data["usage_metrics"]["last_30_days"])


    # 404 response
    def test_retrieve_tool_with_invalid_id(self):
        url = reverse("tool-detail", args=[self.NOT_FOUND_TOOL_ID])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    # 400 response
    def test_retrieve_tool_with_invalid_id_type(self):
        url = reverse("tool-detail", args=["invalid_id"])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data["detail"], "Invalid tool ID.")