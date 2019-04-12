'''
Description - Reports Filters
@author - John Sentz
@date - 15-Nov-2018
@time - 8:48 PM
'''

import django_filters as filters

from . models import Report


class ReportListFilter(filters.FilterSet):

    site = filters.ChoiceFilter(empty_label='SITE', choices=Report.SITE_CHOICES)
    department = filters.ChoiceFilter(empty_label='DEPARTMENT', choices=Report.DEPT_CHOICES)
    program = filters.ChoiceFilter(empty_label='PROGRAM', choices=Report.PROGRAM_CHOICES)

    class Meta:
        model = Report
        fields = ['report_user',
                  'site',
                  'department',
                  'program']

        order_by = ['pk']

    def __init__(self, *args, **kwargs):
        super(ReportListFilter, self).__init__(*args, **kwargs)
        self.filters['report_user'].extra.update(
            {'empty_label': 'STAFF MEMBER'})
