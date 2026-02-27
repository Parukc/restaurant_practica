from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .models import Tables, Orders
from .serializers import TableSerializer, OrderSerializer
from .permissions import IsAdminOrReadOnly

class TablesViewSet(viewsets.ModelViewSet):
    queryset = Tables.objects.all().order_by("id")
    serializer_class = TableSerializer
    permission_classes = [IsAdminOrReadOnly]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ["name"]
    ordering_fields = ["id", "name","capacity","created_at"]

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Orders.objects.select_related("table_id").all().order_by("-id")
    serializer_class = OrderSerializer
    permission_classes = [IsAdminOrReadOnly]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ["table_id"]
    search_fields = ["items_summary", "table_id__name"]
    ordering_fields = ["id", "total", "status", "created_at"]

    def get_queryset(self):
        qs = super().get_queryset()
        anio_min = self.request.query_params.get("anio_min")
        anio_max = self.request.query_params.get("anio_max")
        if anio_min:
            qs = qs.filter(anio__gte=int(anio_min))
        if anio_max:
            qs = qs.filter(anio__lte=int(anio_max))
        return qs

    def get_permissions(self):
        # Público: SOLO listar vehículos
        if self.action == "list":
            return [AllowAny()]
        return super().get_permissions()