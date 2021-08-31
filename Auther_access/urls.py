from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from Auther_access import views

urlpatterns = [
    path('',views.home,name='home'),
    path('dashboard/', views.Dashboard,name='dashboard'),
    path('login/', LoginView.as_view(),name='login_url'),
    path('register/', views.Register,name='register_url'),
    path('logout', LogoutView.as_view(next_page='dashboard'),name='logout_url'),
    path('home', views.Homepage, name='homepage'),
    path('Books', views.BBooks, name='Books'),
    path('upload/', views.Upload, name='upload'),
    path('delete/<int:pk>/', views.Delete, name='delete'),

]
