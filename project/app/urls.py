from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.siswa_create, name='siswa_create'),
    path('read/', views.siswa_read, name='siswa_read'),
    path('update/<int:id>/', views.siswa_update, name='siswa_update'),
    path('delete/<int:id>/', views.siswa_delete, name='siswa_delete'),
]
