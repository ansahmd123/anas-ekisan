from django.urls import path
from . import views
from admin_notification.views import check_notification_view

urlpatterns = [
    path('forget/',views.forget,name="forget"),
    path('',views.home,name="home"),
    path('index/',views.index,name="index"),
    path('password/',views.password,name="password"),
    path('otp/',views.otp,name="otp"),
    path('register/',views.register,name="register"),
    #path('subscription/',views.subscription,name="subscription"),
    #path('success/', views.success, name='success'),
    path('logout/', views.logout, name='logout'),
    path('check/notification', check_notification_view, name="check_notifications"),

]