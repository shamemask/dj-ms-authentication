from django.db import models

class PromoCode(models.Model):
    code = models.CharField(max_length=255, unique=True)
    discount = models.DecimalField(max_digits=5, decimal_places=2)
    expiration_date = models.DateField()

    def __str__(self):
        return self.code
