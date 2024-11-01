from django.db import models

class Products(models.Model):
    user_name = models.CharField(max_length=255)
    product_name = models.CharField(max_length=255)
    product_rating=models.DecimalField(blank=True, null=True, max_digits=10, decimal_places=10)
    user_comment=models.CharField(max_length=400)

