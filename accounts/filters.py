import django_filters
from .models import User


class UserListFilter(django_filters.FilterSet):
    class Meta:
        model = User
        fields = ['username',
                  'email',
                  ]

        order_by = ['pk']
