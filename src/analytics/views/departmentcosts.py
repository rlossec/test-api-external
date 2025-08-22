
from datetime import date

from django.db.models import Sum, Count, Avg, Q
from rest_framework.views import APIView
from rest_framework.response import Response

from toolsmanagement.models import CostTracking




class DepartmentCostsAnalyticsView(APIView):
    def get(self, request):
        # data
        # Liste des owner_department avec pour chaque :
        ## 1. Le coût total cumulé des tools avec ce owner_department
        ## 2. Le nombre de tools de ce département
        ## 3. Le nombre d'utilisateurs des outils de ce owner_department
        ## cost_percentage = (department.total_cost / company_total_cost) * 100
        ## average_cost_per_tool = total_cost / tools_count


        # summary
        ## 1. calcul de la somme des couts dans CostTracking
        total_cost = CostTracking.objects.total_company_cost()
        ## 2. Calcul du nombre de owner_department différent
        ## 3. Calcul du owner_department le plus couteux

        return Response({"data": [], "summary": {"total_cost": total_cost}})