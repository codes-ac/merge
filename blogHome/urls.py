from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.index, name="home"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('search/', views.search, name="search"),
    path('signup/', views.signup, name="signup"),
    path('login/', views.userlogin, name="userlogin"),
    path('logout/', views.userlogout, name="userlogout"),
]