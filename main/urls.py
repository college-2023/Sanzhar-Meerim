from django.template.defaulttags import url
from django.urls import path
from django.views.generic import RedirectView

from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('home', views.home, name='home'),
                  path('staff', views.staff, name='staff'),
                  path('clients', views.clients, name='clients'),
                  path('overview', views.overview, name='overview'),
                  path('analytics', views.analytics, name='analytics'),
                  path('finance', views.finance, name='finance'),
                  path('payroll', views.payroll, name='payroll'),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
