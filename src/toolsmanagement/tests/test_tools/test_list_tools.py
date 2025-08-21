from rest_framework.reverse import reverse

from .test_tools import ToolTestCase


class TestListTools(ToolTestCase):

    def test_list_tools(self):
        url = reverse("tool-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]["name"], "Test Tool 1")
        self.assertEqual(response.data[1]["name"], "Test Tool 2")

