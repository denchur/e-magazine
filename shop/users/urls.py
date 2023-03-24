from django.contrib.auth.views import (
    LogoutView,
    LoginView
)
from django.urls import path

from . import views


app_name = 'users'


urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    path(
        'login/',
        LoginView.as_view(template_name='pages/login/index.html'),
        name='login'
    ),
    path(
        'logout/',
        LogoutView.as_view(template_name='pages/logout/index.html'),
        name='logout'
    ),


]