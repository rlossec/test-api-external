from django.db import models
from django.core.validators import MinValueValidator

from .basemodel import BaseModel
from .tool import Tool


class CostTracking(BaseModel):
    tool = models.ForeignKey(Tool, on_delete=models.CASCADE, related_name='cost_tracking')
    month_year = models.DateField(help_text="Mois/année du suivi de coût")
    total_monthly_cost = models.DecimalField(max_digits=10, decimal_places=2,
                                             help_text="Coût mensuel total incluant licence + surcoûts")
    class Meta:
        unique_together = ['tool', 'month_year']
        ordering = ['-month_year']
        verbose_name = "Monthly cost tracking"

    def __str__(self):
        return f"{self.tool.name} - {self.month_year.strftime('%B %Y')}"

    @property
    def base_monthly_cost(self):
        """Coût mensuel de base de l'outil"""
        return self.tool.base_monthly_cost

    @property
    def additional_costs(self):
        """Surcoûts additionnels"""
        return self.total_monthly_cost - self.base_monthly_cost
    
    @property
    def active_users_count(self):
        """Nombre d'utilisateurs actifs calculé dynamiquement"""
        return self.tool.active_users_count

