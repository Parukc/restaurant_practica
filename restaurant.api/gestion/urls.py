from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import TablesViewSet, OrderViewSet
from .menu_views import menus_types_list_create, menus_types_detail
from .order_events_views import order_event_list_create, order_event_detail

router = DefaultRouter()
router.register(r"tables", TablesViewSet, basename="tables")
router.register(r"orders", OrderViewSet, basename="orders")

urlpatterns = [
    path("menus/", menus_types_list_create),
    path("menus//", menus_types_detail),
    path("order-events/", order_event_list_create),
    path("order-events//", order_event_detail),
]

urlpatterns += router.urls