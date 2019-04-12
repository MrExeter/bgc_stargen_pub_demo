from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


class LoginRequiredView(LoginRequiredMixin):
    login_url = '/accounts/login/'


class TestPage(TemplateView):
    template_name = 'test.html'


class DashboardPage(LoginRequiredMixin, TemplateView):
    template_name = 'accounts/dashboard.html'
    login_url = '/accounts/login/'
    # redirect_field_name = 'login'


class ThanksPage(TemplateView):
    template_name = 'thanks.html'


class HomePage(LoginRequiredMixin, TemplateView):
    login_url = '/accounts/login/'
    template_name = 'index.html'
