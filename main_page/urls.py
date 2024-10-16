
from django.urls import path
from . import views

urlpatterns=[
    path('',views.Home,name='home'),
    path('login',views.Login,name='login'),
    path('signup',views.Signup,name='signup'),
    path('About us',views.About,name='about'),
    path('logout',views.Logout,name='logout'),
    path('contact',views.contact,name='contact'),
    path('Products',views.product,name='product'),

]