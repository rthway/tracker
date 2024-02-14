from django.db import models

class GeneratedSerialNumber(models.Model):
    product_name = models.CharField(max_length=100)
    lots = models.CharField(max_length=6)
    bundle_id = models.CharField(max_length=20)
    serial_number = models.CharField(max_length=20)

    def __str__(self):
        return self.serial_number
