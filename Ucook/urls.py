from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # need to change the path

    path('', views.login_action, name='home'),
    path('login', views.login_action, name='login'),
    path('logout', views.logout_action, name='logout'),
    path('welcome', views.welcome_action, name='welcome'),
    path('register', views.register_action, name='register'),
    path('iAmHost', views.iAmHost_action, name='iAmHost'),
    path('iAmNonHost', views.iAmNonHost_action, name='iAmNonHost'),
    path('exploreHost', views.explorehost_action, name='exploreHost'),
    path('exploreNonHost', views.explorenonhost_action, name='exploreNonHost'),
    path('profile', views.profile_action, name='profile'),
    path('detail', views.detail_action, name='detail'),
    path('mypost', views.mypost_action, name='mypost'),
]

