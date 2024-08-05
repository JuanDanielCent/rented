from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.signin, name='login'),
    path('logout/', views.signout, name='logout'),
    path('venta/', views.venta, name='venta'),
    path('alquiler/', views.alquiler, name='alquiler'),
    path('add_property/', views.add_property, name='add_property'),
    path('add_lease/', views.add_lease, name='add_lease'),
    path('elegir_categoria/', views.elegir_categoria, name='elegir_categoria'),
    path('update_venta/<int:pk>', views.update_venta, name='update_venta'),
    path('delete_venta/<int:pk>', views.delete_venta, name='delete_venta'),
    path('update_alquiler/<int:pk>', views.update_alquiler, name='update_alquiler'),
    path('delete_alquiler/<int:pk>', views.delete_alquiler, name='delete_alquiler')
]