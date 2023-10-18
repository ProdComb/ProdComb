from django.db import models

class Product(models.Model):
    class Types(models.TextChoices):
        SOFTWARE = "sw"
        HARDWARE = "hw"

    type = models.CharField(
        max_length=2,
        choices=Types.choices,
    )

    name = models.CharField(max_length=200)
    vendor = models.CharField(max_length=200)
    id_str = models.CharField('Unique Identifier', max_length=200, blank=True)
