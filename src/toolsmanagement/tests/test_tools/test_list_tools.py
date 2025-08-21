# python manage.py test toolsmanagement.tests.test_tools.test_list_tools

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

    # 200 response

    ## Test list tools with filter
    ### Unique Filters among : name, owner_department, category, min_monthly_cost, max_monthly_cost
    def test_list_tools_with_name_filter(self):
        url = reverse("tool-list")
        response = self.client.get(url, {"name": "Test Tool 1"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["name"], "Test Tool 1")
    
    def test_list_tools_with_owner_department_filter(self):
        url = reverse("tool-list")
        response = self.client.get(url, {"owner_department": "EN"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["owner_department"], "EN")
    
    def test_list_tools_with_category_filter(self):
        url = reverse("tool-list")
        response = self.client.get(url, {"category": self.category_1.id})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["category"], self.category_1.id)
        
    def test_list_tools_with_min_monthly_cost_filter(self):
        url = reverse("tool-list")
        response = self.client.get(url, {"min_monthly_cost": 100})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]["base_monthly_cost"], 100)
        self.assertEqual(response.data[1]["base_monthly_cost"], 200)
      
    def test_list_tools_with_max_monthly_cost_filter(self):
        url = reverse("tool-list")
        response = self.client.get(url, {"max_monthly_cost": 200})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["base_monthly_cost"], 100)
        
    ### Test list tools with multiple filters
    def test_list_tools_with_multiple_filters(self):
        url = reverse("tool-list")
        response = self.client.get(url, {"name": "Test Tool 1", "owner_department": "EN", "category": self.category_1.id, "min_monthly_cost": 100, "max_monthly_cost": 200})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["name"], "Test Tool 1")
        self.assertEqual(response.data[0]["owner_department"], "EN")
        self.assertEqual(response.data[0]["category"], self.category_1.id)
        self.assertEqual(response.data[0]["base_monthly_cost"], 100)

    ## Test sort tools
    ### Sorting : name, , base_monthly_cost, created_at
    
    def test_list_tools_with_name_sorting(self):
        url = reverse("tool-list")
        response = self.client.get(url, {"ordering": "name"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]["name"], "Test Tool 1")
        self.assertEqual(response.data[1]["name"], "Test Tool 2")

    def test_list_tools_with_base_monthly_cost_sorting(self):
        url = reverse("tool-list")
        response = self.client.get(url, {"ordering": "base_monthly_cost"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]["base_monthly_cost"], 100)
        self.assertEqual(response.data[1]["base_monthly_cost"], 200)
    
    def test_list_tools_with_created_at_sorting(self):
        url = reverse("tool-list")
        response = self.client.get(url, {"ordering": "created_at"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]["created_at"], self.tool_1.created_at)
        self.assertEqual(response.data[1]["created_at"], self.tool_2.created_at)
    
    ## Test No result case clearly
    def test_list_tools_with_no_result(self):
        url = reverse("tool-list")
        response = self.client.get(url, {"name": "Nonexistent Tool"})
        self.assertEqual(response.status_code, 200)
        self.assertIn("detail", response.data)
        self.assertEqual(response.data["detail"], "No tools found matching with this criterias.")


 