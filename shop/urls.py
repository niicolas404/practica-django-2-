from django.urls import path

from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('<str:pelicula>/<int:id>/', views.detalle, name='detalle'),
]
