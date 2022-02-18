from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('mypage/', views.mypage, name="mypage"),
    path('description/', views.description, name="description"),
    path('overview/', views.overview, name="overview"),
    path('enrolled/', views.enrolled, name="enrolled"),

    path('', views.home, name = "home"),
]