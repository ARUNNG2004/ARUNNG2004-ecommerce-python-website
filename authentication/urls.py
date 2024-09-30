from django.urls import path
from .views import *

urlpatterns = [


        path('',Loginpage),
        path('logout/',LogoutUser),
        path('signup/', SignupPage),
]
