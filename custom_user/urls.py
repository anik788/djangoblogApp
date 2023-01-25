from django.urls import path
from django.contrib.auth.views import LogoutView
from custom_user.views import UserCreateView, UserLoginView, UserProfileDetailView

app_name = 'custom_user'

urlpatterns = [
    path('signup/', UserCreateView.as_view(), name='signup'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/<int:pk>/', UserProfileDetailView.as_view(), name='profile')
]
