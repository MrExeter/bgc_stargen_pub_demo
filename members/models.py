'''
Description - Members model
@author - John Sentz
@date - 15-Nov-2018
@time - 6:43 PM
'''

from datetime import date
from django.conf import settings
from django.urls import reverse
from django.core.validators import MinLengthValidator, RegexValidator
from django.db import models
from django.utils import timezone

try:
    from django.contrib.auth import get_user_model

    User = settings.AUTH_USER_MODEL
except ImportError:
    from django.contrib.auth.models import User

from django import template

register = template.Library()


class Member(models.Model):
    GENDER_CHOICES = (
        ('Girl', 'Girl'),
        ('Boy', 'Boy')
    )

    numeric = RegexValidator(r'^[1-9][0-9]*$', 'Must be numeric and cannot begin with zero.')
    member_number = models.CharField('Member Number',
                                     max_length=4,
                                     validators=[MinLengthValidator(3), numeric],
                                     unique=True)

    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    gender = models.CharField(max_length=4, default=None, choices=GENDER_CHOICES, verbose_name='Gender')
    birth_date = models.DateField(default=timezone.localdate(timezone.now()))

    def __str__(self):
        identity = self.member_number + ' - ' + self.first_name + ' ' + self.last_name
        return identity

    def save(self, *args, **kwargs):
        # Capitalize first and last names before saving
        for field_name in ['first_name', 'last_name']:
            val = getattr(self, field_name, False)
            if val:
                setattr(self, field_name, val.lower().capitalize())
            super(Member, self).save(*args, **kwargs)

    def get_absolute_url(self):
        # return reverse('members:all')
        return reverse('member:detail', kwargs={'pk': self.pk})

    def get_age(self):
        today = date.today()
        return today.year - self.birth_date.year - (
                (today.month, today.day) < (self.birth_date.month, self.birth_date.day))

