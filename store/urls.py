from django.urls import path
from . import views

urlpatterns = [
    path('', views.ShowStoresList.as_view()),
    path('<int:pk>', views.ShowStore.as_view()),
]
