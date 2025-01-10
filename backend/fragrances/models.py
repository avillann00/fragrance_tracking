from django.db import models
from django.contrib.auth.models import User

class Fragrance(models.Model):
    # house, name, website, url, id, user(foreign key), notes
    id = models.BigAutoField(primary_key=True)
    house = models.CharField(max_length=225)
    name = models.CharField(max_length=225)
    notes = models.CharField(max_length=225)
    website = models.CharField(max_length=225)
    url = models.URLField(max_length=225)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} by {self.house}'

class Price(models.Model):
    # fragrance(foreign key), id, price, date/time, name
    id = models.BigAutoField(primary_key=True)
    fragrance = models.ForeignKey(Fragrance, null=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=225)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.fragrance} costs ${self.price} on {self.date}'

