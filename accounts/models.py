########################################################################################################################
#
# OLD user model based on Django User
#
# from django.db import models
# from django.contrib import auth
#
#
# # Create your models here.
# class User(auth.models.User, auth.models.PermissionsMixin):
#
#     def __str__(self):
#         return "@{}".format(self.username)

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.urls import reverse
# from django.core.urlresolvers import reverse


def save(self, *args, **kwargs):
    # Capitalize first and last names before saving
    for field_name in ['first_name', 'last_name']:
        val = getattr(self, field_name, False)
        if val:
            setattr(self, field_name, val.lower().capitalize())
        super(User, self).save(*args, **kwargs)
        # super().save(*args, **kwargs)


# Custom staff models
class UserStaffProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    has_admin_privilege = models.BooleanField(default=False)

    def __str__(self):
        return 'Profile for user {}'.format(self.user.username)


def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_staff_profile = UserStaffProfile.objects.create(user=kwargs['instance'])
        user_staff_profile.first_name = sender.first_name
        user_staff_profile.last_name = sender.last_name


def __str__(self):
    return self.first_name + ' ' + self.last_name


def get_absolute_url(self):
    # return reverse('members:all')
    return reverse('accounts:detail', kwargs={'pk': self.pk})


post_save.connect(create_profile, sender=User)

