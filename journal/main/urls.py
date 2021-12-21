from django.urls import path
from .views import MainView, RegisterUser, LoginUser, LogoutUser
urlpatterns = [
    path('home', MainView.as_view(), name='home'),
    path('register', RegisterUser.as_view(), name='register'),
    path('login', LoginUser.as_view(), name='login'),
    path('logout', LogoutUser.as_view(), name='logout')
]

