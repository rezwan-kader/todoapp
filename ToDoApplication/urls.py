from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('account/', views.account, name='account'),
    path('userlogin/', views.userlogin, name='userlogin'),
    path('logout/', views.logout, name='logout'),
]
