from django.urls import path, include
from . import views

urlpatterns = [
    path('signup/',views.signup,name='signup'),
    path('login/',views.userlogin,name='login'),
    path('',views.home_view,name='home'),
]
