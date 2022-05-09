from django.urls import path
from .views import ShowProductsListView, ShowProductView, CreateProductsView
urlpatterns = [
    path('products_list', ShowProductsListView.as_view()),
    path('add_new_product', CreateProductsView.as_view()),
    path('<int:pk>', ShowProductView.as_view())
]
