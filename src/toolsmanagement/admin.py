from django.contrib import admin
from .models.tool import Tool
from .models.category import Category
from .models.toolaccess import UserToolAccess
from .models.access_request import AccessRequest
from .models.cost import CostTracking
from .models.usage import UsageLog


admin.site.register(Tool)
admin.site.register(Category)
admin.site.register(UserToolAccess)
admin.site.register(AccessRequest)
admin.site.register(CostTracking)
admin.site.register(UsageLog)
