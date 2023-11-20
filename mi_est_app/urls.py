from django.urls import path
from . import views

app_name = 'mi_est_app'
urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('estacionamientos/', views.estacionamientos, name='estacionamientos'),
    path('estacionamiento/<int:id>',
         views.estacionamiento, name='estacionamiento'),
    path('nuevo_estacionamiento/', views.nuevo_arriendo,
         name='nuevo_estacionamiento'),
    path('editar_arriendo/<int:id>',
         views.editar_arriendo, name='editar_arriendo'),
    path('eliminar_arriendo/<int:id>',
         views.elimiar_arriendo, name='eliminar_arriendo'),
    path('ver_estacionamiento/<int:id>',
         views.ver_estacionamiento, name='ver_estacionamiento'),
    path('estacionamiento_arrendado/<int:id>',
         views.estacionamiento_arrendado, name='estacionamiento_arrendado'),
    path('arriendos/', views.arriendos, name='arriendos'),
    path('arriendo/<int:id>', views.arriendo, name='arriendo'),
]
