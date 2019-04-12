from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User

from django.urls import reverse_lazy

from django.views.generic import CreateView, UpdateView, DetailView, ListView
from django_tables2 import RequestConfig

from accounts.filters import UserListFilter
from accounts.tables import UserTable
from accounts.utils import PagedFilteredTableView
from .forms import UserCreateForm, UserEditForm, UserListFormHelper
# from settings_secret import SOCIAL_AUTH_GOOGLE_OAUTH2_KEY as GOOGLE_OAUTH2

class UserIndexView(LoginRequiredMixin, ListView):
    template_name = 'accounts/index.html'
    context_object_name = 'all_users'

    login_url = '/accounts/login/'

    # redirect_field_name = 'login'

    def get_queryset(self):
        return User.objects.all()


# Create your views here.
class SignUp(CreateView):
    # declare simple form
    form_class = UserCreateForm
    # upon successful user creation, redirect to login page
    success_url = reverse_lazy('login')
    login_url = '/accounts/login/'

    template_name = 'accounts/signup.html'


class EditUserProfile(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserEditForm
    template_name = 'accounts/edit.html'
    login_url = '/accounts/login/'

    success_url = reverse_lazy('dashboard')

    def get_object(self, *args, **kwargs):
        # user = get_object_or_404(User, pk=self.kwargs['pk'])

        # We can also get user object using self.request.user  but that doesnt work
        # for other models.

        return self.request.user


class UserListView(LoginRequiredMixin, PagedFilteredTableView):
    model = User
    template_name = 'accounts/user_list.html'
    login_url = '/accounts/login/'
    context_object_name = 'user'
    ordering = ['-id']
    # group_required = u'company-user'
    table_class = UserTable
    filter_class = UserListFilter
    formhelper_class = UserListFormHelper

    def get_queryset(self):
        # return User.objects.all()
        qs = super(UserListView, self).get_queryset()
        return qs

    def post(self, request, *args, **kwargs):
        return PagedFilteredTableView.as_view()(request)

    def get_context_data(self, **kwargs):
        context = super(UserListView, self).get_context_data(**kwargs)
        context['nav_member'] = True
        search_query = self.get_queryset()
        table = UserTable(search_query)
        RequestConfig(self.request, paginate={'per_page': 10}).configure(table)
        context['table'] = table
        user = self.request.user

        context['user'] = user

        return context


class UserDetailView(LoginRequiredMixin, DetailView):
    model = User
    login_url = '/accounts/login/'
    template_name = 'accounts/user_detail.html'



