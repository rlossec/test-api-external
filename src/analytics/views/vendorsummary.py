from rest_framework.views import APIView
from rest_framework.response import Response


class VendorSummaryAnalyticsView(APIView):
    def get(self, request):
        return Response({"data": []})