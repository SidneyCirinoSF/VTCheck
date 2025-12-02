from django.urls import path
from . import views

app_name = 'police_car'

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('editar/<uuid:id>/', views.editar_viatura, name='editar'),
    path('deletar/<uuid:id>/', views.deletar_viatura, name='deletar'),
]
