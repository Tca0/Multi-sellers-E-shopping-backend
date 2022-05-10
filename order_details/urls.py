from django.urls import path
from order_details.views import ReplaceCustomerOrdersListView, MyOrdersListView


urlpatterns = [
    path("myorders", MyOrdersListView.as_view()),
    path("neworder", ReplaceCustomerOrdersListView.as_view())
]
