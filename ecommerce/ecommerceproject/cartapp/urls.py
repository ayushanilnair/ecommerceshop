from django.urls import path
from . import views

app_name='cartapp'

urlpatterns=[
     path('add/<int:product_id>/',views.Addcart,name='Addcart'),
     path('remove/<int:product_id>/',views.cart_remove,name='cart_remove'),
     path('delete/<int:product_id>/',views.full_remove,name='full_remove'),
     path('',views.Detailcart,name='Detailcart'),

]