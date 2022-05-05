from django.urls import path
from .views import RegisterView, UserUpdateDeleteProfileView, UserProfileView
#from django.views.generic.base import RedirectView
# from dj_rest_auth.registration.serializers import RegisterSerializer


urlpatterns = [
    path('register', RegisterView.as_view()),
    # for view account add view profile allow admin+anyuser
    # for update delete and allow the profile owner or admin
    path('profile/<int:pk>', UserUpdateDeleteProfileView.as_view()),
    path('users/<int:pk>', UserProfileView.as_view())

]
