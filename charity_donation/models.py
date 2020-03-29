from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name


INSTITUTION_TYPE = ((0, 'Fundacja'),
                    (1, 'Organizacja pozarządowa'),
                    (2, 'Zbiórka lokalna'))


class Institution(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField()
    categories = models.ManyToManyField(Category)
    type = models.IntegerField(choices=INSTITUTION_TYPE, default=0)

    def __str__(self):
        return self.name


class Donation(models.Model):
    quantity = models.IntegerField()
    categories = models.ManyToManyField(Category)
    institution = models.ManyToManyField(Institution)
    address = models.TextField()
    phone_number = models.IntegerField()
    city = models.CharField(max_length=128)
    zip_code = models.CharField(max_length=6)
    pickup_date = models.DateField()
    pickup_time = models.TimeField()
    pickup_comment = models.CharField(max_length=140)
    collected = models.BooleanField(default=False, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"Oddano organizacji {self.institution.name}"





