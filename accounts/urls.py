from django.conf.urls import url
from django.urls import path, include
from django.contrib.auth import views as auth_views
# from django.urls import reverse_lazy
from django.urls import reverse_lazy

from . import views

app_name = 'accounts'

urlpatterns = [
    url(r'^login/$', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),
    url(r'^signup/$', views.SignUp.as_view(success_url=reverse_lazy('accounts:login')), name='signup'),
    url(r'^edit/$', views.EditUserProfile.as_view(), name='edit'),

    url(r'^$', views.UserIndexView.as_view(), name='index'),

    url(r'account/userlist/$', views.UserListView.as_view(), name='user-list'),
    url(r'^(?P<pk>[0-9]+)/$', views.UserDetailView.as_view(), name='detail'),

    # change password
    url(r'^password-change/$',
        auth_views.PasswordChangeView.as_view(success_url=reverse_lazy('accounts:password_change_done')),
        name='password_change'),

    url(r'^password-change/done/$', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),

    # change and reset password
    url(r'^password-reset/$',
        auth_views.PasswordResetView.as_view(success_url=reverse_lazy('accounts:password_reset_done')),
        name='password_reset'),
    url(r'^password-reset/done/$',
        auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),

    url(r'^password-reset/confirm/(?P<uidb64>[-\w]+)/(?P<token>[-\w]+)/$',
        auth_views.PasswordResetConfirmView.as_view(success_url=reverse_lazy('accounts:login')),
        name='password_reset_confirm'),

    url(r'^password-reset/complete/$',
        auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'),
        name='password_reset_complete'),

]
