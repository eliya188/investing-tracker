from django.db import models
import datetime

class Investment(models.Model):
    name = models.CharField(max_length=150, blank=False)
    start_date = models.DateField(blank=False)
    deposit_money = models.FloatField(blank=False)
    current_money = models.FloatField(blank=False)