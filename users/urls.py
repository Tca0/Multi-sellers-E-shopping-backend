from django.urls import path
from .views import RegisterCustomerView, BecomeVendorView

urlpatterns = [
    path('register', RegisterCustomerView.as_view()),
    path('open-store', BecomeVendorView.as_view()),
]
