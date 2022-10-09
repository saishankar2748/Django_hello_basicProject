from django.contrib import admin
from django.urls import path
from home import views

#username - demo    pass - demodemo
#username - demo1    pass - demo1demo1

urlpatterns = [
    path("",views.index,name="home"),
    path("about",views.about,name="about"),
    path("service",views.service,name="service"),
    path("contact/",views.contact,name="contact"),
    path("login",views.loginUser,name="login"),
    path("logout",views.logoutUser,name="logout"),
]
