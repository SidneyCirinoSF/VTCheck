from django.urls import path
from . import views

app_name = 'user'

urlpatterns = [
    path('', views.pagina_login, name='login'),
    path('cadastro/', views.pagina_cadastro, name='cadastro'),
    path('logout/', views.fazer_logout, name='logout'),
]