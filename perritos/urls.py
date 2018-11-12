from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.register, name='register'),
    path('index', views.index, name='index'),
    path('quienes', views.quienes, name='quienes'),
    path('contacto', views.contacto, name='contacto'),
    path('nuevo', views.nuevo, name='nuevo'),
    path('mostrar2', views.mostrar2, name='mostrar2'),
    path('adoptado', views.adoptado, name='adoptado'),
    path('mostrarcontacto', views.mostrarcontacto, name='mostrarcontacto'),
    url(r'^user_login/$',views.user_login,name='user_login'),
]
