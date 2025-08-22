from datetime import datetime

from django.db import models
from django.contrib.auth import get_user_model

from .basemodel import BaseModel
from .tool import Tool


User = get_user_model()

class AccessRequest(BaseModel):
    STATUS_CHOICES = [
        ('PE', 'Pending'),
        ('AP', 'Approved'),
        ('RE', 'Rejected'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='access_requests')
    tool = models.ForeignKey(Tool, on_delete=models.CASCADE, related_name='access_requests')
    business_justification = models.TextField(blank=True)
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default='pending')
    processed_at = models.DateTimeField(null=True, blank=True)
    processed_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='requests_processed', null=True, blank=True)
    processing_notes = models.TextField(blank=True)

    class Meta:
        ordering = ['-created_at']
        unique_together = ['user', 'tool', 'status']

    def __str__(self):
        return f"{self.user.username} - {self.tool.name} ({self.status})"

    @property
    def requested_at(self):
        """Date de demande (alias pour created_at)"""
        return self.created_at

    def approve(self, approved_by_user, notes=""):
        """Approuve la demande d'accès"""
        self.status = 'approved'
        self.processed_by = approved_by_user
        self.processing_notes = notes
        self.save()

    def reject(self, rejected_by_user, notes=""):
        """Rejette la demande d'accès"""
        self.status = 'rejected'
        self.processed_at = datetime.now()
        self.processed_by = rejected_by_user
        self.processing_notes = notes
        self.save()

    