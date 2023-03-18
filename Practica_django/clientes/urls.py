from django.urls import path
from  . import views
urlpatterns = [
    path('', views.inicio,name='inicio'),
    path('listado_clientes' , views.list_clientes, name='clientes'),
    
    
]
