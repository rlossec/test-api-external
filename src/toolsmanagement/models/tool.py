from datetime import date

from django.db import models
from django.db.models import Count, Sum, Avg, Q

from .basemodel import BaseModel
from .category import Category


class ToolManager(models.Manager):
    def tools_by_department(self):
        """Retourne tous les outils par département"""
        return self.values('owner_department').annotate(tools_count=Count('id'))


class Tool(BaseModel):
    STATUS_CHOICES = [
        ('AC', 'Active'),
        ('TR', 'Trial'),
        ('DE', 'Deprecated'),
    ]

    DEPARTMENT_CHOICES = [
        ('EN', 'Engineering'),
        ('SA', 'Sales'),
        ('MK', 'Marketing'),
        ('HR', 'HR'),
        ('FI', 'Finance'),
        ('OP', 'Operations'),
        ('DE', 'Design')
    ]

    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    vendor = models.CharField(max_length=100, null=False)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='tools')
    base_monthly_cost = models.DecimalField(max_digits=10, decimal_places=2,
                                            help_text="Coût mensuel de base de l'outil (licence)")
    website_url = models.URLField(blank=True)
    owner_department = models.CharField(max_length=2, choices=DEPARTMENT_CHOICES)
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default='AC')

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    @property
    def active_users_count(self):
        """Nombre d'utilisateurs actuellement actifs sur cet outil"""
        return self.user_accesses.filter(revoked_at__isnull=True).count()

    @property
    def is_active(self):
        """Vérifie si l'outil est actif"""
        return self.status == 'AC'

    @property
    def total_monthly_cost(self):
        """Coût mensuel total réel incluant les surcoûts"""
        current_month = date.today().replace(day=1)
        cost_tracking = self.cost_tracking.get(month_year=current_month)
        return cost_tracking.total_monthly_cost

    def get_active_users(self):
        """Retourne tous les utilisateurs actuellement actifs"""
        return self.user_accesses.filter(revoked_at__isnull=True).select_related('user')
    
    objects = ToolManager()
