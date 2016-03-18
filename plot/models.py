import datetime

from django.db import models
from django.utils import timezone

class Stock(models.Model):
    stock_name = models.CharField(max_length=200)
    lookup_symbol = models.CharField(max_length=50, primary_key=True)

    def __str__(self):
        return self.stock_name + ':' + self.lookup_symbol