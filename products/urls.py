from django.urls import path
from .views import ShowProductsListView, ShowProductView, CreateProductsView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
# ShowPSellerroductsListView
urlpatterns = [
    path('', ShowProductsListView.as_view()),
    path('<int:pk>', ShowProductView.as_view()),
    # seller routs
    #path('seller', ShowPSellerroductsListView.as_view()),
    path('seller', CreateProductsView.as_view()),
]
urlpatterns += staticfiles_urlpatterns()
