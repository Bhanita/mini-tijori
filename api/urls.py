from django.urls import path

from . import views

urlpatterns = [
    path('investor/<int:sid>/', views.get_investor),
    path('investor/list/', views.get_all_investors),
    path('investor/list/<int:sid>/', views.get_all_by_id),
    path('create/', views.create_investor),
    path('company/list/', views.get_all_companies),
]
