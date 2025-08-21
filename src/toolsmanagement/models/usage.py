from django.db import models
from django.contrib.auth import get_user_model

from .basemodel import BaseModel
from .tool import Tool


User = get_user_model()

class UsageLog(BaseModel):
    tool = models.ForeignKey(Tool, on_delete=models.CASCADE, related_name='usage_logs')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='usage_logs')
    session_date = models.DateField()
    usage_minutes = models.IntegerField()
    actions_count = models.IntegerField()

    class Meta:
        ordering = ['-session_date']
        unique_together = ['tool', 'user', 'session_date']

    def __str__(self):
        return f"{self.user.username} - {self.tool.name} ({self.session_date})"
