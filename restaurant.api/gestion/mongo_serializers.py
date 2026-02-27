from rest_framework import serializers


class MenuSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=120)
    category = serializers.CharField(max_length=80, required=False, allow_blank=True)
    price = serializers.FloatField()
    is_available = serializers.BooleanField(default=True)


class OrderEventSerializer(serializers.Serializer):
    EVENT_CHOICES = ["CREATED", "UPDATED", "PAID", "CANCELED"]
    SOURCE_CHOICES = ["API", "ADMIN", "SYSTEM"]

    order_id = serializers.IntegerField()  # ID de Orders (Postgres)
    event_type = serializers.ChoiceField(choices=EVENT_CHOICES)
    source = serializers.ChoiceField(choices=SOURCE_CHOICES)
    note = serializers.CharField(required=False, allow_blank=True)
    created_at = serializers.DateTimeField(required=False)