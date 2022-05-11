"""UAFD_PRO URL Configuration

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
from uafd_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name="home"),
    path('about/',views.about,name="about"),
    path('management/',views.management,name="management"),
    path('aboutsociety/',views.aboutsociety,name="aboutsociety"),
    path('vision/',views.vision,name="vision"),
    path('services/',views.services,name="services"),
    path('activities/',views.activities,name="activities"),
    path('recent_activities/',views.recent_activities,name="recent_activities"),
    path('upcoming_activities/',views.upcoming_activities,name="upcoming_activities"),
    path('members/',views.members,name="members"),
    path('terms/',views.terms,name="terms"),
    path('notifications/',views.notifications,name="notifications"),
    path('contact/',views.contact,name="contact"),
    path('login/',views.login_view,name="login"),
    path('signup/',views.signup,name="signup"),
    path('logout/',views.logout_view,name="logout"),
    path('applicationform/',views.applicationform,name="applicationform")
]
