from rest_framework import serializers
from .models import Tables, Orders

class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tables
        fields = ["id", "name", "capacity", "is_avaliable", "created_at"]

class OrderSerializer(serializers.ModelSerializer):
    table_name = serializers.CharField(source="table_id.name", read_only=True)

    class Meta:
        model = Orders
        fields = ["id", "table_id", "table_name", "items_summary", "total", "status", "created_at"]