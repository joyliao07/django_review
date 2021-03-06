"""forms_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, include
from forms_app import views


urlpatterns = [
    path('', views.home_view, name="home"),
    path('cbv', views.CBView.as_view()),
    path('cbvt', views.CBVTemplate.as_view()),
    path('forms_app/', include('forms_app.urls', namespace='forms_app')),
    path('showtopic', views.show_topic, name="show topic"),
    path('testforms', views.testform_view, name="test forms"),
    path('userprofile', views.userprofile_view, name="user profile"),
    path('register', views.register, name="register"),
    path('login', views.login_view, name="login"),
    path('logout', views.logout_view, name="logout"),
    path('admin/', admin.site.urls),
]
