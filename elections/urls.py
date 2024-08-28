from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='elections_home'),
    path('lgas/', views.LgaListView.as_view(), name='elections_lgas'),
    path('pu_results_form/', views.polling_unit_results, name='pu_results_form'),
    path('lga_form/', views.lga_form, name='lga_form'),
    path('polling_units_results_sum/', views.polling_units_results_sum, name='polling_units_results_sum'),
]