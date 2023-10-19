from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=200)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    search_term = models.CharField(max_length=200, unique=True)
    full_name = models.CharField(max_length=200)
    vendor = models.CharField(max_length=200)

    def __str__(self):
        return self.search_term or self.name + " by " + self.vendor

class Combination(models.Model):
    class Status(models.IntegerChoices):
        UNUSABLE = 0, "Unusable"
        USABLE = 1, "Usable but has significant issues"
        GOOD = 2, "Works good but has some minor issues"
        PERFECT = 3, "Works perfectly with no issues"


    name = models.CharField(max_length=200)
    products = models.ManyToManyField(Product)
    status = models.IntegerField(
        choices=Status.choices,
    )

    def __str__(self):
        return self.name
