from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    path('profile/<int:user_id>/', views.user_profile, name='user_profile'),
    path('send_message/', views.send_direct_message, name='send_direct_message'),
    path('inbox/', views.inbox_view, name='inbox_view'),
    path('read_message/<int:message_id>/', views.read_message, name='read_message'),

]