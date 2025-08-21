
from django.db import models
from django.contrib.auth import get_user_model

from .basemodel import BaseModel
from .tool import Tool

User = get_user_model()

class UserToolAccess(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tool_accesses')
    tool = models.ForeignKey(Tool, on_delete=models.CASCADE, related_name='user_accesses')
    granted_at = models.DateTimeField()
    granted_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='accesses_granted')
    revoked_at = models.DateTimeField(null=True, blank=True)
    revoked_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='accesses_revoked', null=True, blank=True)

    class Meta:
        unique_together = ['user', 'tool']
        ordering = ['-granted_at']

    def __str__(self):
        status = "Actif" if self.is_active else "Révoqué"
        return f"{self.user.username} - {self.tool.name} ({status})"

    @property
    def status(self):
        """Statut calculé de l'accès"""
        if self.revoked_at:
            return 'revoked'
        return 'active'

    @property
    def is_active(self):
        """Vérifie si l'accès est actuellement actif"""
        return self.revoked_at is None

    def revoke_access(self, revoked_by_user):
        """Révoque l'accès à l'outil"""
        from datetime import datetime
        self.revoked_at = datetime.now()
        self.revoked_by = revoked_by_user
        self.save()

