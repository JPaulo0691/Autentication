from django.conf.urls import url
from django.urls import path
from django.contrib.auth import views as auth_views
from .import views

urlpatterns = [
    #view de login
    path('login/', auth_views.LoginView.as_view(), name = 'login'),
    path('logout/', auth_views.LogoutView.as_view(), name = 'logout'),
    path('',views.dashboard, name = 'dashboard'),
    path('password_change/', auth_views.PasswordChangeView.as_view(), name = 'password_change'),
    path('password_change_done/', auth_views.PasswordChangeDoneView.as_view(), name = 'password_change_done'), 
    #This path will show to the user a success message  after the user change his password. After all, create a template for each view.

]
