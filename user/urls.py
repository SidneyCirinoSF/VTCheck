from django.urls import path, reverse_lazy
from django.contrib.auth import views as auth_views
from . import views

app_name = 'user'

urlpatterns = [
    path('', views.pagina_login, name='login'),
    path('cadastro/', views.pagina_cadastro, name='cadastro'),
    path('logout/', views.fazer_logout, name='logout'),
    path('password_change/', auth_views.PasswordChangeView.as_view(success_url=reverse_lazy('user:password_change_done')), name='password_change'),
    path('password_change_done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('password_reset/', auth_views.PasswordResetView.as_view(success_url=reverse_lazy('user:password_reset_done')), name='password_reset'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(success_url=reverse_lazy('user:password_reset_complete')), name='password_reset_confirm'),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]