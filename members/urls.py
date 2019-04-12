'''
Description - Member URLS
@author - John Sentz
@date - 15-Nov-2018
@time - 7:25 PM
'''

from django.conf.urls import url
from . import views

app_name = 'members'

urlpatterns = [
    # url(r'^$', views.IndexView.as_view(), name='index'),
    # url(r'^$', views.MemberListView.as_view(), name='index'),

    url(r'member/memberlist/$', views.MemberListView.as_view(), name='member-list'),

    url(r'^(?P<pk>[0-9]+)/$', views.MemberDetail.as_view(), name='detail'),

    # /members/member/add/
    url(r'member/add/$', views.CreateMember.as_view(), name='member-add'),

    # /members/member/2/
    url(r'member/(?P<pk>[0-9]+)/$', views.UpdateMember.as_view(), name='member-update'),

    # /members/delete/2/delete/
    url(r'member/(?P<pk>[0-9]+)/delete/$', views.DeleteMember.as_view(), name='member-delete'),
]
