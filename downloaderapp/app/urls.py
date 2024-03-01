
from django.urls import path
from app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('login', views.loginUser, name='login'),
    path('signup', views.signupUser, name='signup'),
    path('service',views.service,name='service'),
    path('contact',views.contact, name='contact'),
    path('logout', views.logoutUser, name='logoutUser'),    
]