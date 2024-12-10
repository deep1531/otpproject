
from django.urls import path
from .views import login_view ,otp_view , main_view ,logout_view




urlpatterns = [
    path('', main_view,name='main'),
    path('login/',login_view,name='login'),
    path('otp/',otp_view,name='otp'),
    path('logout/',logout_view,name='logout'),
]