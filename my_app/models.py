from django.db import models


class Device(models.Model):

    choices = (
        ('AVAILABLE', 'Item ready to be purchased'),
        ('SOLID', 'Item Sold'),
        ('RESTOCKING', 'Item restocking in few days')
    )


    type = models.CharField(max_length=100, blank=False)
    price = models.IntegerField()
    status = models.CharField(max_length=10, choices=choices, default="SOLD")
    issues = models.CharField(max_length=100, default="No issues")

    class Meta:
        abstract = True

    def __str__(self):
        return f'Type: {self.type} Price:{self.price}'


class Desktop(Device):
    pass


class Laptop(Device):
    pass


class Mobile(Device):
    pass