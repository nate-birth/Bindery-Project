from django.urls import path
from . import views

urlpatterns = [
    path('', views.store, name="store"),
    path('product/<int:pid>', views.productPage, name="product"),
    path('add', views.add_to_cart, name="add")
]