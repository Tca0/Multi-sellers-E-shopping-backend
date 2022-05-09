from django.urls import path
from . import views
urlpatterns = [
    path('', views.ShowCategoriesList.as_view()),
    path('newcategory', views.AddCategory.as_view()),
    path('<int:pk>', views.ShowCategory.as_view()),
]
