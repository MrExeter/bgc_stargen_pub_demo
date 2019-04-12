'''
Description - Reports Model
@author - John Sentz
@date - 15-Nov-2018
@time - 8:47 PM
'''

from django.db import models
from django.utils import timezone

from accounts.models import User
from members.models import Member


# Create your models here.
class Report(models.Model):
    SITE_CHOICES = (
        ('PAC', 'Performing Arts Center'),
        ('Slavik', 'Slavik'),
        ('M-S', 'MacKenzie-Scott')
    )

    DEPT_CHOICES = (
        ('Music', 'Music'),
        ('Games', 'Games'),
        ('Education/Learning', 'Education/Learning'),
        ('Teen', 'Teen'),
        ('Athletics/Aquatics', 'Athletics/Aquatics'),
        ('Art', 'Art'),
        ('Tech', 'Tech'),
        ('Other', 'Other'),
    )

    PROGRAM_CHOICES = (
        ('Project Learn', 'Project Learn'),
        ('Power Hour', 'Power Hour'),
        ('Club Tech', 'Club Tech'),
        ('College Bound', 'College Bound'),
        ('Money Matters', 'Money Matters'),
        ('Career Launch', 'Career Launch'),
        ('Torch Club', 'Torch Club'),

        ('Keystone Club', 'Keystone Club'),
        ('Triple Play', 'Triple Play'),
        ('SMART Moves', 'SMART Moves'),
        ('SMART Girls', 'SMART Girls'),
        ('Passport to Manhood', 'Passport to Manhood'),
        ('NetSmartz', 'NetSmartz'),
        ('Image Makers', 'Image Makers'),

        ('Clay Tech', 'Clay Tech'),
        ('Drama Matters', 'Drama Matters'),
        ('Music', 'Music'),
        ('Aquatics', 'Aquatics'),
        ('Youth of the Year', 'Youth of the Year'),
        ('OTHER', 'OTHER'),
    )

    report_date = models.DateField(default=timezone.localdate(timezone.now()))
    site = models.CharField(max_length=24, default=None, choices=SITE_CHOICES, verbose_name='Site')
    department = models.CharField(max_length=24, choices=DEPT_CHOICES, verbose_name='Department')
    report_complete = models.BooleanField(default=False)
    program = models.CharField(max_length=48, choices=PROGRAM_CHOICES, verbose_name='Program')
    summary = models.TextField(max_length=2000, blank=True)
    feedback_challenges = models.TextField(max_length=2000, blank=True)
    # report_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, verbose_name='Employee')
    report_user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name='Employee')
    members = models.ManyToManyField(Member, related_name='members', blank=True)

    def __str__(self):
        if self.report_user is None:
            identity = self.report_date.strftime("%d-%b-%y") + ' - ' + \
                       "First" + ' ' + \
                       "Last" + ' : ' + \
                       self.program
        else:
            identity = self.report_date.strftime("%d-%b-%y") + ' - ' + \
                       self.report_user.first_name.capitalize() + ' ' + \
                       self.report_user.last_name.capitalize() + ' : ' + \
                       self.program

        return identity

    def get_day_of_report(self):
        tags = {0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday', 4: 'Friday', 5: 'Saturday',
                6: 'Sunday'}

        pony = self.report_date.weekday()
        # return tags[self.report_date.weekday()]
        return tags[pony]

    def get_employee_name(self):
        if self.report_user.first_name is not None and self.report_user.last_name is not None:
            return self.report_user.first_name.lower().capitalize() + ' ' + self.report_user.last_name.lower().capitalize()
        else:
            return "No Name"

    def get_age_and_gender_buckets(self):

        young = [6, 7, 8, 9]
        tween = [10, 11, 12]
        teens = [13, 14, 15, 16, 17, 18]
        a = 'G69'  # Girls 6-9 years old
        b = 'B69'  # Boys 6-9 years old
        c = 'GTWEEN'  # Girls 10-12 years old
        d = 'BTWEEN'  # Boys 10-12 years old
        e = 'GTEEN'  # Girl Teens 13-18
        f = 'BTEEN'  # Boy Teens 13-18
        g = 'TOTALYOUNG'  # Total 6-9 year old
        h = 'TOTALTWEEN'  # Total 10-12 year old
        i = 'TOTALTEEN'  # Total Teenagers 13-18

        demographics = {a: 0, b: 0, c: 0, d: 0, e: 0, f: 0, g: 0, h: 0, i: 0}

        for member in self.members.all():
            age = member.get_age()
            gender = member.gender

            if gender == 'Girl':
                if age in young:
                    demographics[a] += 1
                elif age in tween:
                    demographics[c] += 1
                else:
                    demographics[e] += 1
            else:
                if age in young:
                    demographics[b] += 1
                elif age in tween:
                    demographics[d] += 1
                else:
                    demographics[f] += 1

            demographics[g] = demographics[a] + demographics[b]
            demographics[h] = demographics[c] + demographics[d]
            demographics[i] = demographics[e] + demographics[f]

        return demographics

