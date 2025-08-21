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
    

    # 400 response
    ## Mandatory fields : name, owner_department, vendor, category, base_monthly_cost
    def test_create_tool_without_mandatory_fields(self):
        url = reverse("tool-list")
        mandatory_fields = ["name", "owner_department", "vendor", "category", "base_monthly_cost"]
        for field in mandatory_fields:
            body = self.body.copy()
            body.pop(field)
            response = self.client.post(url, body)
            self.assertEqual(response.status_code, 400)
            self.assertEqual(response.data[field], "This field is required.")
    
    ## Validation errors

    ### name : This field may have between 2 and 100 characters.
    def test_create_tool_with_invalid_name(self):
        url = reverse("tool-list")
        invalids_names = ["", "a", "a" * 101]
        for name in invalids_names:
            body = self.body.copy()
            body["name"] = name
            response = self.client.post(url, body)
            self.assertEqual(response.status_code, 400)
            self.assertEqual(response.data["name"], "This field may have between 2 and 100 characters.")

    ### base_monthly_cost : This field is a decimal field with 2 decimal places and strictly positive.
    def test_create_tool_with_invalid_base_monthly_cost(self):
        url = reverse("tool-list")
        invalids_base_monthly_costs = ["", -1, 0, 1.001, "a"]
        for base_monthly_cost in invalids_base_monthly_costs:
            body = self.body.copy()
            body["base_monthly_cost"] = base_monthly_cost
            response = self.client.post(url, body)
            self.assertEqual(response.status_code, 400)
            self.assertEqual(response.data["base_monthly_cost"], "This field is a decimal field with 2 decimal places and strictly positive.")

    ### website_url : URL must be a valid URL.
    def test_create_tool_with_invalid_website_url(self):
        url = reverse("tool-list")
        invalids_website_urls = ["", "a", "a" * 101]
        for website_url in invalids_website_urls:
            body = self.body.copy()
            body["website_url"] = website_url
            response = self.client.post(url, body)
            self.assertEqual(response.status_code, 400)
            self.assertEqual(response.data["website_url"], "Enter a valid URL.")
    
    ### category_id : in Database
    def test_create_tool_with_invalid_category_id(self):
        url = reverse("tool-list")
        body = self.body.copy()
        body["category"] = self.NOT_FOUND_CATEGORY_ID
        response = self.client.post(url, body)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data["category"], "Invalid category ID.")

    ### vendor : This fiels may have between 1 and 100 characters.
    def test_create_tool_with_invalid_vendor(self):
        url = reverse("tool-list")
        invalids_vendors = ["" "a" * 101]
        for vendor in invalids_vendors:
            body = self.body.copy()
            body["vendor"] = vendor
            response = self.client.post(url, body)
            self.assertEqual(response.status_code, 400)
            self.assertEqual(response.data["vendor"], "This field may have between 1 and 100 characters.")
