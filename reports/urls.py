'''
Description - Reports URLs
@author - John Sentz
@date - 15-Nov-2018
@time - 9:05 PM
'''


from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'reports'

urlpatterns = [
    url(r'^$', views.ReportIndexView.as_view(), name='index'),

    # url(r'member/memberlist/$', views.MemberListView.as_view(), name='member-list'),
    url(r'report/reportlist/$', views.ReportListView.as_view(), name='report-list'),

    url(r'^(?P<pk>[0-9]+)/$', views.ReportDetailView.as_view(), name='detail'),

    # /reports/report/add/
    url(r'report/add/$', views.CreateReportView.as_view(), name='report-add'),

    # /reports/report/2/
    url(r'report/(?P<pk>[0-9]+)/$', views.UpdateReportView.as_view(), name='report-update'),

    # /members/delete/2/delete/
    url(r'report/(?P<pk>[0-9]+)/delete/$', views.DeleteReportView.as_view(), name='report-delete'),

    # url(r'report/(?P<pk>[0-9]+)/pdf/$', GeneratePDF.as_view(), name='report-pdf'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG == True:
    urlpatterns += staticfiles_urlpatterns()
