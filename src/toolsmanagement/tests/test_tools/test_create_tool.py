# python manage.py test toolsmanagement.tests.test_tools.test_create_tool

from rest_framework import status
from rest_framework.reverse import reverse

from .test_tools import ToolTestCase


class TestCreateTool(ToolTestCase):

    def test_create_tool(self):
      url = reverse("tool-list")
      response = self.client.post(url, self.create_body)
      self.assertEqual(response.status_code, status.HTTP_201_CREATED)
      self.assertEqual(response.data["name"], "Test Create UpdateTool 1")
      self.assertEqual(response.data["website_url"], "https://test-create-update-tool-1.com")
      self.assertEqual(response.data["description"], "Test Create Update Description 1")
      self.assertEqual(response.data["owner_department"], "EN")
      self.assertEqual(response.data["vendor"], "Test Create Update Vendor 1")
      self.assertEqual(response.data["category"], self.category_1.id)
      self.assertEqual(response.data["base_monthly_cost"], 100.00)
    

    # 400 response
    ## Mandatory fields : name, owner_department, vendor, category, base_monthly_cost
    def test_create_tool_without_mandatory_fields(self):
        url = reverse("tool-list")
        mandatory_fields = ["name", "owner_department", "vendor", "category", "base_monthly_cost"]
        for field in mandatory_fields:
            with self.subTest(missing_field=field):
                body = self.create_body.copy()
                body.pop(field)
                response = self.client.post(url, body)
                self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
                self.assertIn("This field is required.", response.data[field])
    
    ## Validation errors
    ### name : This field may have between 2 and 100 characters.
    def test_create_tool_with_invalid_name(self):
        url = reverse("tool-list")
        invalid_names = ["", "a", "a" * 101]
        for name in invalid_names:
            with self.subTest(invalid_name=name):
                body = self.create_body.copy()
                body["name"] = name
                response = self.client.post(url, body)
                self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
                self.assertEqual(
                    response.data["name"],
                    "This field may have between 2 and 100 characters."
                )

    ### base_monthly_cost : This field is a decimal field with 2 decimal places and strictly positive.
    def test_create_tool_with_invalid_base_monthly_cost(self):
        url = reverse("tool-list")
        invalid_costs = ["", -1, 0, 1.001, "a"]
        for cost in invalid_costs:
            with self.subTest(invalid_cost=cost):
                body = self.create_body.copy()
                body["base_monthly_cost"] = cost
                response = self.client.post(url, body)
                self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
                self.assertEqual(
                    response.data["base_monthly_cost"],
                    "This field is a decimal field with 2 decimal places and strictly positive."
                )
    
    ### website_url : URL must be a valid URL.
    def test_create_tool_with_invalid_website_url(self):
        url = reverse("tool-list")
        invalid_urls = [
            "",
            "not-an-url",
            "http:/incomplete.com",
            "http://??.com",
            "http://exa mple.com",
        ]
        for url in invalid_urls:
            with self.subTest(invalid_url=url):
                body = self.create_body.copy()
                body["website_url"] = url
                response = self.client.post(url, body)
                self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
                self.assertEqual(response.data["website_url"], "Enter a valid URL.")
    
    ### category_id : in Database
    def test_create_tool_with_invalid_category_id(self):
        url = reverse("tool-list")
        body = self.create_body.copy()
        body["category"] = self.NOT_FOUND_ID
        response = self.client.post(url, body)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data["category"], "Invalid category ID.")

    ### vendor : This fiels may have between 1 and 100 characters.
    def test_create_tool_with_invalid_vendor(self):
        url = reverse("tool-list")
        invalid_vendors = ["", "a" * 101]
        for vendor in invalid_vendors:
            with self.subTest(invalid_vendor=vendor):
                body = self.create_body.copy()
                body["vendor"] = vendor
                response = self.client.post(url, body)
                self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
                self.assertEqual(
                    response.data["vendor"],
                    "This field may have between 1 and 100 characters."
                )
