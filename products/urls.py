from django.urls import path
from . import views
urlpatterns = [
    path('', views.ShowProductsList.as_view()),
    path('<int:pk>', views.ShowProduct.as_view())
]
