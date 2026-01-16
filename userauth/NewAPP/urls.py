from django.urls import path

from . import views

urlpatterns = [

    path('', views.homepage,name=""),
    path('register', views.register,name="register"),
    path('my_Login', views.my_Login,name="my_Login"),
    path('dashboard', views.dashboard,name="dashboard"),

]







 
















