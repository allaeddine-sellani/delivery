# contacts/urls.py
from django.urls import path
from . import views

urlpatterns = [
    
    path('get_items/',views.get_items,name='get_items'),
     path('', views.menu, name='menu'),
    path('manage_clients/', views.manage_clients, name='manage_clients'),
    path('manage_clients/add/', views.add_client, name='add_client'),
    path('manage_stores/', views.manage_stores, name='manage_stores'),
    path('manage_stores/add/', views.add_store_item, name='add_store'),
    path('manage_drivers/', views.manage_drivers, name='manage_drivers'),
    path('manage_drivers/add/', views.add_driver, name='add_driver'),
    path('manage_clients/edit/<int:client_id>/', views.edit_client, name='edit_client'),
    path('manage_stores/edit/<int:store_id>/', views.edit_store_item, name='edit_store'),
    path('manage_drivers/edit/<int:driver_id>/', views.edit_driver, name='edit_driver'),
    path('cmd/',views.add_CMD,name='cmd'),
]
