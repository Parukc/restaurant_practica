from django.db import models

class Tables(models.Model):
    name = models.CharField(max_length=50, unique=True)
    capacity = models.IntegerField()
    is_avaliable = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)



    def __str__(self):
        return self.name

class Orders(models.Model):
    table_id = models.ForeignKey(Tables, on_delete=models.PROTECT, related_name="orders")
    items_summary = models.CharField(max_length=120)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    class Status(models.TextChoices):
        PENDING ="pending", "Pending"
        IN_PROGRESS = "in_progress", "In_Progress"
        SERVED = "served" , "Served"
        PAID = "paid" , "Paid"

    status = models.CharField(max_length=20, choices=Status.choices, default=Status.PENDING)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.id} - Mesa {self.table_id_id}"