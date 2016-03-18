import datetime

from django.db import models
from django.utils import timezone
from django import forms
# Create your models here.

class Blog(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    title = models.CharField(max_length=100)
    data = models.CharField(max_length=300)
    pub_date = models.DateTimeField(default=timezone.now())


    def __str__(self):
        return self.data

    def was_published_recently(self):
        return timezone.now() >= self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'