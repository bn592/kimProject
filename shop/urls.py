from django.urls import path

from shop import views

urlpatterns = [
    path('product_write',views.product_write),
    path('product_insert',views.product_insert),
    path('product_list',views.product_list),

]