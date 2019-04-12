'''
Description - Member Admin
@author - John Sentz
@date - 15-Nov-2018
@time - 7:42 PM
'''

from django.contrib import admin
from . models import Member


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    # date_hierarchy = 'birth_date'

    list_display = ["member_number", "first_name", "last_name", "gender", "age", "birth_date"]
    list_filter = ["gender"]

    search_fields = ['member_number', "first_name", "last_name"]

    def age(self, obj):
        return obj.get_age()

