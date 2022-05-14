from django.contrib import admin
from django.urls import include, path
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include("rest_framework.urls")),
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    # path for register using a dj-rest-auth
    #path('dj-rest-auth/registration/',include('dj_rest_auth.registration.urls'), name='register'),
    path("api/token", jwt_views.TokenObtainPairView.as_view(),  # access token + refresh token
         name="token_obtain_pair"),
    path('api/token/refresh', jwt_views.TokenRefreshView.as_view(),  # new access token
         name="token_refresh"),
    path('categories/', include('categories.urls')),
    path('products/', include('products.urls')),
    path('', include('users.urls')),
    path('orders/', include("order_details.urls")),
]
