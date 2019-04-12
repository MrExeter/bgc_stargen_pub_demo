'''
Description - Member Filter
@author - John Sentz
@date - 15-Nov-2018
@time - 7:11 PM
'''

import django_filters as filters
from .models import Member


class MemberListFilter(filters.FilterSet):

    # member_number = filters.AllValuesFilter()
    # last_name = filters.AllValuesFilter()
    gender = filters.ChoiceFilter(empty_label='GENDER', choices=Member.GENDER_CHOICES)

    class Meta:
        model = Member
        fields = ['member_number',
                  'first_name',
                  'last_name',
                  'gender',
                  'birth_date']
        order_by = ['pk']
    #
    # def __init__(self, *args, **kwargs):
    #     super(MemberListFilter, self).__init__(*args, **kwargs)
    #     self.filters['member_number'].extra.update(
    #         {'empty_label': 'MEMBER ID'})
