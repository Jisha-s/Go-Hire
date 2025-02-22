from django.urls import path
from . import views


urlpatterns = [
    path('',views.HomePage, name='HomePage'),
    path('UserCreation/',views.CreateUserAccount, name='CreateUserAccount'),
    path('Loginuser/',views.LoginUser, name='LoginUser'),
    path('ForgotPassword/',views.ForgotPassword, name='ForgotPassword'),
    path('UpdatePassword/', views.UpdatePassword, name='UpdatePassword')

]