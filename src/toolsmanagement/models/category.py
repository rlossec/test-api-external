from django.db import models
from django.db.models import Sum
from .basemodel import BaseModel


class Category(BaseModel):
    name = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=100)
    color_hex = models.CharField(max_length=7)

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

    @property
    def tools_count(self):
        """Nombre d'outils dans cette catégorie"""
        return self.tools.count()

    @property
    def active_tools_count(self):
        """Nombre d'outils actifs dans cette catégorie"""
        return self.tools.filter(status='AC').count()

    @property
    def total_monthly_cost(self):
        """Coût mensuel total de tous les outils de cette catégorie"""
        return self.tools.aggregate(
            total_cost=Sum('monthly_cost')
        )['total_cost'] or 0
