from django.urls import path
from . import views

app_name='ecommerceapp'

urlpatterns = [
    path('',views.allProductCat,name='allProductCat'),
    path('<slug:c_slug>/',views.allProductCat,name='product_by_category'),
    path('<slug:c_slug>/<slug:product_slug>/', views.prodDetail, name='prodCatDetail')
]