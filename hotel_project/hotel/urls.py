from os import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('rooms/', views.room_lists, name='room_lists'),
    path('rooms/<uuid:room_id>/', views.single_room, name='single_room'),
    path('rooms/<uuid:room_id>/booking/', views.room_booking, name='room_booking'),
    path('rooms/<uuid:room_id>/booking/payment/', views.room_payment, name='room_payment'),
    path('rooms/<uuid:room_id>/checking/', views.room_checkin, name='room_checkin'),
    path('rooms/<uuid:room_id>/checkout/', views.room_checkout, name='room_checkout'),
    path('login/', views.admin_login, name='admin_login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('admin/', views.admin_list, name='admin_list'),
    path('admin/create/', views.show_admin, name='show_admin'),
    path('admin/<uuid:staff_id>/edit/', views.edit_admin, name='edit_admin'),
    path('admin/<uuid:staff_id>/delete/', views.delete_admin, name='delete_admin'),
    path('admin/logs/', views.logs, name='logs'),
]