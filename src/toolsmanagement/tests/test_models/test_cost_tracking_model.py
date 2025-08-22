# python manage.py test toolsmanagement.tests.test_models.test_cost_tracking_model
from datetime import datetime
from decimal import Decimal

from django.test import TestCase
from django.contrib.auth import get_user_model
from django.utils import timezone

from ...models import (
    Category, Tool, UserToolAccess, CostTracking
)

User = get_user_model()

class CostTrackingTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(
            name="Test Category",
            description="Test Description",
            color_hex="#FF0000"
        )

        self.tool_1 = Tool.objects.create(
            name="Test Tool 1",
            description="Test Description",
            vendor="Test Vendor 1",
            category=self.category,
            base_monthly_cost=Decimal('10.00'),
            owner_department='EN',
            status='AC'
        )

        self.tool_2 = Tool.objects.create(
            name="Test Tool 2",
            description="Test Description",
            vendor="Test Vendor 1",
            category=self.category,
            base_monthly_cost=Decimal('12.00'),
            owner_department='EN',
            status='AC'
        )

        self.tool_3 = Tool.objects.create(

            name="Test Tool 3",
            description="Test Description",
            vendor="Test Vendor 2",
            category=self.category,
            base_monthly_cost=Decimal('15.00'),
            owner_department='MK',
            status='AC'
        )

        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )

    def test_active_users_count_property(self):
        """Test de la propriété active_users_count"""
        cost_tracking = CostTracking.objects.create(
            tool=self.tool_1,
            month_year=datetime.today(),
            total_monthly_cost=Decimal('10.00')
        )

        # Aucun utilisateur actif au début
        self.assertEqual(cost_tracking.active_users_count, 0)

        # Créer un accès actif
        UserToolAccess.objects.create(
            user=self.user,
            tool=self.tool_1,
            granted_at=timezone.now(),
            granted_by=self.user
        )

        self.assertEqual(cost_tracking.active_users_count, 1)


    def test_total_monthly_cost_property(self):
        """Test de la propriété total_monthly_cost"""
        ## Ajout de 3 CostTracking pour le mois de juin 2025
        cost_tracking_1 = CostTracking.objects.create(
            tool=self.tool_1,
            month_year=datetime(2025, 6, 1),
            total_monthly_cost=Decimal('124.00')
        )
        cost_tracking_2 = CostTracking.objects.create(
            tool=self.tool_2,
            month_year=datetime(2025, 6, 1),
            total_monthly_cost=Decimal('10.00')
        )
        cost_tracking_3 = CostTracking.objects.create(
            tool=self.tool_3,
            month_year=datetime(2025, 6, 1),
            total_monthly_cost=Decimal('15.99')
        )
        total_monthly_cost = cost_tracking_1.total_monthly_cost + cost_tracking_2.total_monthly_cost + cost_tracking_3.total_monthly_cost
        self.assertEqual(CostTracking.objects.total_company_cost(), total_monthly_cost)

