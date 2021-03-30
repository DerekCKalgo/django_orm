from django.db import models

class Store(models.Model):
    quantity = models.IntegerField()
    productid = models.IntegerField()
    price = models.FloatField(default=19.99)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
