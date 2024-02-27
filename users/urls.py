from django.urls import path
from . import views
from .views import view_signup,view_verifyemail


app_name = "users"

urlpatterns = [
    path('login', views.view_login, name="login"),
    path('logout', views.view_logout, name="logout"),
    path('signup',  view_signup, name="signup"),
    path('verifyemail',  view_verifyemail, name="verifyemail"),
]
