from django.urls import path

from . import views

urlpatterns = [
    path('person/<int:sid>/', views.get_person),
    path('person/list/', views.get_details),
    path('person/list/<int:sid>/', views.get_all_by_id),
    path('create/', views.create_person),
    path('company/list/', views.get_all_companies),
]
