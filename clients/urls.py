# clients/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # CRUD URLs
    path('dashboard/', views.dashboard, name='dashboard'),
    path('add/', views.add_client, name='add_client'),
    path('update/<int:pk>/', views.update_client, name='update_client'),
    path('delete/<int:pk>/', views.delete_client, name='delete_client'),

    # AUTH URLs - Add these
    path('register/', views.register_user, name='register'),
    path('', views.login_user, name='login'), # Set login as the root page
    path('logout/', views.logout_user, name='logout'),
]