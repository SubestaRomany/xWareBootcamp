
from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home , name ="home"),
    path('about_us/',views.about_us,name="about_us"),
    path('fac_info/',views.faculty_info,name="fac_info")
]
