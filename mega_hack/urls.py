"""mega_hack URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from faculty.views import *
from student1.views import *
from mentor.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',homepage_display,name='homepage_display'),
    path('fac_login/',faculty_login_view,name='faculty_login'),
    path('mentor_login/',mentor_login_view,name='mentor_login'),
    path('std_login/',student_login_view,name='std_login'),
    path('fac_profile/<fac_id>/',faculty_profile_view,name='faculty_profile'),
    path('mentor_profile/<fac_id>/',mentor_profile_view,name='mentor_profile'),
    path('std_profile/<std_id>/',student_profile_display,name='student_profile'),
    path('std_info/<std_id>/',faculty_std_academic_view,name='std_academic'),
    path('std_attend/<fac_id>/',faculty_student_attendance,name='std_attend'),
    path('aboutus/',about_us,name='about_us')
]
