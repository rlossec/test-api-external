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
        self.assertEqual(response.data["owner_department"], "EN")
        self.assertEqual(response.data["vendor"], "Test Vendor")
        self.assertEqual(response.data["category"], self.category_1.id)