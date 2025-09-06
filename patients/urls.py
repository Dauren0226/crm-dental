from django.urls import path
from . import views

app_name = 'patients'

urlpatterns = [
    path('add/', views.add_patient, name='add_patient'),
    path('', views.patient_list, name='patient_list'),
    path('edit/<int:pk>/', views.edit_patient, name='edit_patient'),
    path('<int:pk>/delete/', views.delete_patient, name='delete_patient'),
    path('<int:pk>/', views.patient_detail, name='patient_detail'),
    path('<int:pk>/add_visit/', views.add_visit, name='add_visit'),
]
