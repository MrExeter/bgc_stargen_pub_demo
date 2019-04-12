'''
Description - Reports Views
@author - John Sentz
@date - 15-Nov-2018
@time - 9:05 PM
'''


from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView
from django_tables2 import RequestConfig

from accounts.models import UserStaffProfile
from reports.tables import ReportTable
from reports.utils import PagedFilteredTableView
from .filters import ReportListFilter
from .forms import ReportListFormHelper, ReportCreateOrUpdateForm
from .models import Report


# Create your views here.
class ReportIndexView(LoginRequiredMixin, ListView):
    model = Report
    login_url = '/accounts/login/'
    user = get_user_model()
    template_name = 'reports/index.html'

    context_object_name = 'all_reports'

    def get_queryset(self):
        user = self.request.user
        return Report.objects.all()


class ReportDetailView(LoginRequiredMixin, DetailView):
    user = get_user_model()
    model = Report
    login_url = '/accounts/login/'
    template_name = 'reports/report_detail.html'


class CreateReportView(LoginRequiredMixin, CreateView):
    user = get_user_model()
    model = Report()
    login_url = '/accounts/login/'
    template_name = 'reports/report_form.html'
    form_class = ReportCreateOrUpdateForm
    success_url = reverse_lazy('reports:report-list')

    def form_valid(self, form, **kwargs):
        report = form.save(commit=False)
        report.report_user = self.request.user
        # if request == 'POST':

        report.save()
        form.save_m2m()
        # report.save(commit=False)
        # report.save_m2m()
        # report.save()

        return HttpResponseRedirect(self.success_url)


class UpdateReportView(LoginRequiredMixin, UpdateView):
    model = Report
    login_url = '/accounts/login/'
    template_name = 'reports/report_update.html'
    form_class = ReportCreateOrUpdateForm
    success_url = reverse_lazy('reports:report-list')


class DeleteReportView(LoginRequiredMixin, DeleteView):
    model = Report
    login_url = '/accounts/login/'
    success_url = reverse_lazy('reports:report-list')

    def get_context_data(self, **kwargs):
        context = super(DeleteReportView, self).get_context_data(**kwargs)
        context['next_url'] = self.request.GET.get(
            'next')  # pass `next` parameter received from previous page to the context
        return context

    # def post(self, request, *args, **kwargs):
    #
    #     if request.method == 'POST':
    #         pass
    #
    #     if "Cancel" in request.POST:
    #         url = self.get_success_url()
    #         return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    #     else:
    #         return super(DeleteReportView, self).post(request, *args, **kwargs)


class ReportListView(LoginRequiredMixin, PagedFilteredTableView):

    model = Report
    login_url = '/accounts/login/'
    template_name = 'reports/report_list.html'
    context_object_name = 'report'
    ordering = ['-id']
    table_class = ReportTable
    filter_class = ReportListFilter
    formhelper_class = ReportListFormHelper

    def get_queryset(self):
        user = self.request.user
        user_id = user.id
        staff_user = UserStaffProfile.objects.get(pk=user_id)

        # Retrieve All Reports, check if logged in user has admin privileges, if not, only return the users own reports
        qs = super(ReportListView, self).get_queryset()
        if staff_user.has_admin_privilege:
            return qs
        else:
            return Report.objects.filter(report_user=user)

    def post(self, request, *args, **kwargs):
        return PagedFilteredTableView.as_view()(request)

    def get_context_data(self, **kwargs):

        request_user_id = self.request.user.id

        context = super(ReportListView, self).get_context_data(**kwargs)
        context['nav_member'] = True
        context['request_user_id'] = request_user_id
        search_query = self.get_queryset()
        table = ReportTable(search_query)
        RequestConfig(self.request, paginate={'per_page': 10}).configure(table)
        context['table'] = table

        return context


# class GeneratePDF(LoginRequiredMixin, View):
#     model = Report
#     login_url = '/accounts/login/'
#     template_name = 'pdf/report.html'
#
#     def get(self, request, *args, **kwargs):
#
#         report_id = self.kwargs['pk']
#
#         report = Report.objects.get(pk=report_id)
#
#         # report_user = self.kwargs['report_user.get_full_name.title']
#         # report_date = self.kwargs['report_date']
#         # site = self.kwargs['site']
#         # department = self.kwargs['department']
#         # category = self.kwargs['program']
#         #
#         # total_young = self.kwargs['report.get_age_and_gender_buckets.TOTALYOUNG']
#
#         data = {
#             'report_id': report_id,
#             'report': report,
#
#             'amount': 39.99,
#             'customer_name': 'Cooper Mann',
#             'order_id': 1233434,
#         }
#         pdf = render_to_pdf('pdf/report.html', data)
#         return HttpResponse(pdf, content_type='application/pdf')
