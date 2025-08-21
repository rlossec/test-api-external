
from rest_framework import serializers
from ..models.tool import Tool

class ToolSerializer(serializers.ModelSerializer):
    active_users_count = serializers.IntegerField(read_only=True)


    class Meta:
        model = Tool
        fields = [
            "id",
            "name",
            "description",
            "vendor",
            "category",
            "base_monthly_cost",
            "website_url",
            "owner_department",
            "status",
            "created_at",

            "active_users_count"
        ]
        read_only_fields = ["created_at"]
