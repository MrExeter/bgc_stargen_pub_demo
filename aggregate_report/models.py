'''
Description - Aggregate Report Model
@author - John Sentz
@date - 04-Jan-2019
@time - 10:59
'''

from django.db import models
from django.utils import timezone
from accounts.models import User

class AggregateReport(models.Model):
    pass
    # agg_report_date = models.DateField(default=timezone.localdate(timezone.now()))
    # agg_report_user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name='Employee')


