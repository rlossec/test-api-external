# python manage.py test toolsmanagement.tests.test_models.test_tool_model

from django.test import TestCase
from django.contrib.auth import get_user_model
from django.utils import timezone
from decimal import Decimal

from ...models import (
    Category, Tool, UserToolAccess,
)

User = get_user_model()



class ToolTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(
            name="Test Category",
            description="Test Description",
            color_hex="#FF0000"
        )
        
        self.tool = Tool.objects.create(
            name="Test Tool",
            description="Test Description",
            vendor="Test Vendor",
            category=self.category,
            base_monthly_cost=Decimal('10.00'),
            owner_department='EN',
            status='AC'
        )
        
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )

    def test_active_users_count_property(self):
        """Test de la propriété active_users_count"""
        # Aucun accès actif au début
        self.assertEqual(self.tool.active_users_count, 0)
        
        # Créer un accès actif
        UserToolAccess.objects.create(
            user=self.user,
            tool=self.tool,
            granted_at=timezone.now(),
            granted_by=self.user
        )
        
        self.assertEqual(self.tool.active_users_count, 1)

    def test_tools_by_department(self):
        """Test de la méthode tools_by_department"""
        tools_by_department = Tool.objects.tools_by_department()
        self.assertEqual(list(tools_by_department), [{'owner_department': 'EN', 'tools_count': 1}])






