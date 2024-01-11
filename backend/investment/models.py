from django.db import models
from user.models import Profile
import datetime

class Investment(models.Model):
    # user = models.ForeignKey(Profile, null=True, on_delete=models.CASCADE, related_name='investments')
    name = models.CharField(max_length=150, blank=False)
    start_date = models.DateField(blank=False)
    deposit_money = models.FloatField(blank=False)
    current_money = models.FloatField(blank=False)