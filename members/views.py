'''
Description - Member Views
@author - John Sentz
@date - 15-Nov-2018
@time - 7:24 PM
'''

from django.contrib.auth.mixins import (LoginRequiredMixin)
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView
from django_tables2 import RequestConfig

from members.filters import MemberListFilter
from members.models import Member
from members.utils import PagedFilteredTableView
from .forms import MemberListFormHelper, MemberCreateOrUpdateForm
from .tables import MemberTable, MemberTableLimited


class LoginRequiredMemberView(LoginRequiredMixin):
    login_url = '/accounts/login/'


class IndexView(LoginRequiredMixin, ListView):
    template_name = 'members/index.html'
    login_url = '/accounts/login/'
    context_object_name = 'all_members'

    # def get_queryset(self):
    #     return Member.objects.all()


class MemberDetail(LoginRequiredMixin, DetailView):
    model = Member
    login_url = '/accounts/login/'
    template_name = 'members/member_detail.html'


# Create your views here.
class CreateMember(LoginRequiredMixin, CreateView):
    model = Member
    template_name = 'members/member_form.html'
    # form_class = MemberCreateForm
    form_class = MemberCreateOrUpdateForm

    success_url = reverse_lazy('members:member-list')


class UpdateMember(LoginRequiredMixin, UpdateView):
    model = Member
    login_url = '/accounts/login/'
    template_name = 'members/member_update.html'
    # form_class = MemberUpdateForm
    form_class = MemberCreateOrUpdateForm
    success_url = reverse_lazy('members:member-list')


class DeleteMember(LoginRequiredMixin, DeleteView):
    model = Member
    success_url = reverse_lazy('members:member-list')

#
# class MemberListView(LoginRequiredMixin, ListView):
#   model = Member
#   template_name = 'members/member_list.html'
#   context_object_name = 'member'
#   ordering = ['id']
#
#
#   def get_context_data(self, **kwargs):
#     context = super(MemberListView, self).get_context_data(**kwargs)
#     # context['nav_customer'] = True
#     table = MemberTable(Member.objects.all())
#     RequestConfig(self.request, paginate={'per_page': 10}).configure(table)
#     context['table'] = table
#     return context


class MemberListView(LoginRequiredMixin, PagedFilteredTableView):
    model = Member
    login_url = '/accounts/login/'
    template_name = 'members/member_list.html'
    context_object_name = 'member'
    ordering = ['-id']
    # group_required = u'company-user'
    table_class = MemberTable
    table_class_limited = MemberTableLimited
    filter_class = MemberListFilter
    formhelper_class = MemberListFormHelper

    def get_queryset(self):
        qs = super(MemberListView, self).get_queryset()
        return qs

    def post(self, request, *args, **kwargs):
        return PagedFilteredTableView.as_view()(request)

    def get_context_data(self, **kwargs):
        context = super(MemberListView, self).get_context_data(**kwargs)
        context['nav_member'] = True
        search_query = self.get_queryset()

        user = self.request.user
        if user.userstaffprofile.has_admin_privilege:
            table = MemberTable(search_query)
        else:
            table = MemberTableLimited(search_query)

        RequestConfig(self.request, paginate={'per_page': 10}).configure(table)
        context['table'] = table

        return context

