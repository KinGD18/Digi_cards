from django.urls import path
from . import views

app_name = 'liens'

urlpatterns = [
    # Authentification
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    # Dashboard
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/search/', views.dashboard_search, name='dashboard_search'),
    path('', views.dashboard, name='home'),

    # Gestion des clients
    path('dashboard/client/nouveau/', views.client_create, name='client_create'),
    path('dashboard/client/<int:pk>/', views.client_detail, name='client_detail'),
    path('dashboard/client/<int:pk>/modifier/', views.client_edit, name='client_edit'),
    path('dashboard/client/<int:pk>/toggle/', views.client_toggle_status, name='client_toggle_status'),
    path('dashboard/client/<int:pk>/supprimer/', views.client_delete, name='client_delete'),

    # Gestion des liens
    path('dashboard/client/<int:client_pk>/lien/nouveau/', views.lien_create, name='lien_create'),
    path('dashboard/lien/<int:pk>/modifier/', views.lien_edit, name='lien_edit'),
    path('dashboard/lien/<int:pk>/supprimer/', views.lien_delete, name='lien_delete'),

    # Page publique
    path('p/<str:code_unique>/', views.profil_public, name='profil_public'),
]