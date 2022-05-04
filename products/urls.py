from django.urls import path
from .views import ShowProductsList, ShowProduct, CreateProducts
urlpatterns = [
    path('', ShowProductsList.as_view()),
    path('upload_product', CreateProducts.as_view()),
    path('<int:pk>', ShowProduct.as_view())
]
