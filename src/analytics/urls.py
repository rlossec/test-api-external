from django.urls import path
from .views import DepartmentCostsAnalyticsView, ExpensiveToolsAnalyticsView, LowUsageToolsAnalyticsView, ToolsByCategoryAnalyticsView, VendorSummaryAnalyticsView

urlpatterns = [
  path('department-costs/', DepartmentCostsAnalyticsView.as_view(), name='department-costs'),
  path('expensive-tools/', ExpensiveToolsAnalyticsView.as_view(), name='expensive-tools'),
  path('low-usage-tools/', LowUsageToolsAnalyticsView.as_view(), name='low-usage-tools'),
  path('tools-by-category/', ToolsByCategoryAnalyticsView.as_view(), name='tools-by-category'),
  path('vendor-summary/', VendorSummaryAnalyticsView.as_view(), name='vendor-summary')
]