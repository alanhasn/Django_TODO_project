from django.urls import path
from . import views

app_name = 'main_page'

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('login', views.Login.as_view(), name='login'),
    path('signup', views.Signup.as_view(), name='signup'),
    path('About us', views.About.as_view(), name='about'),
    path('logout', views.Logout.as_view(), name='logout'),  # Assuming Logout is a function-based view
    path('contact', views.contact.as_view(), name='contact'),
    path('Products', views.product.as_view(), name='product'),
    # path('Download Archive app', views.download_app.as_view(), name='download_app'),
]