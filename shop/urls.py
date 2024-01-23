from django.urls import path
from . import views


urlpatterns = [

    path('categorys-get/',views.categorys, name='categorys-get' ),
    path('categorys-get-id/<str:pk>/',views.categorys_get_id, name='categorys-get-id' ),

    path('praducts-get/',views.praducts, name='praducts-get' ),
    path('praduct-get-id/<str:pk>/',views.praduct_get_id, name='praduct-get-id' ),
    
]