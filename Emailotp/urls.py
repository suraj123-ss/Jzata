

from django.urls import path

from . import views



urlpatterns = [
    path('',views.signup,name="signup"),
    path('login',views.login,name="login"),
    path("logout",views.logout_request, name="logout"),  
]