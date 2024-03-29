from django.urls import path

from . import views

urlpatterns = [
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('mypage/', views.mypage, name="mypage"),
    path('description/', views.description, name="description"),
    path('overview/', views.overview, name="overview"),
    path('enrolled/', views.enrolled, name="enrolled"),
    path('about/', views.about, name="about"),
    path('register/', views.registerPage, name="register"),
    path('hike/<str:pk>/', views.hike, name ="hike"),
    path('createhike/', views.createHike, name="createhike"),
    path('updatehike/<str:pk>/', views.updateHike, name="updatehike"),
    path('deletehike/<str:pk>/', views.deleteHike, name="deletehike"),
    path('signuphike/<str:pk>/', views.signupHike, name="signuphike"),
    path('signoffhike/<str:pk>/', views.signoffHike, name="signoffhike"),

    path('', views.home, name = "home"),
]
