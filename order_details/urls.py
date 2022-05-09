from django.urls import path
from order_details.views import CustomerOrdersListView, CustomerOrderView


urlpatterns = [
    path("myorders", CustomerOrdersListView.as_view()),
    path("neworder", CustomerOrderView.as_view())
]
