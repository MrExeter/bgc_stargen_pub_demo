"""bgc_dj_stargen_adv URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from bgc_dj_stargen_adv import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.HomePage.as_view(), name='home'),
    url(r'^accounts/', include('accounts.urls', namespace='accounts')),
    # url(r'^test/$', views.TestPage.as_view(), name='test'),
    url(r'^dashboard/$', views.DashboardPage.as_view(), name='dashboard'),
    url(r'^thanks/$', views.ThanksPage.as_view(), name='thanks'),
    url(r"^members/", include("members.urls", namespace="members")),
    url(r"^reports/", include("reports.urls", namespace="reports")),
    # url(r'^select2/', include('select2.urls')),
    # url(r'^oauth/', include('social_django.urls'), name='social'),
    url(r'^select2/', include('django_select2.urls')),
]
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
