from django.urls import path
from . import views

# Namespace
app_name = 'emp'

# URL Patterns
urlpatterns = [
    # path('', views.welcome_page, name='welcome'),
    # path('login/', views.login_page, name='login'),
    path('', views.welcome_page, name='welcome'),
    path('dashboard/',views.dashboard,name = 'dashboard'),
    path('start/', views.start_work, name='start_work'),
    path('end/<int:session_id>/', views.end_work, name='end_work'),
    path('login/',views.user_login,name = 'user_login'),
    path('logout/',views.user_logout ,name = 'user_logout'),
    path('register/',views.register,name = 'register'),
    path('goodbye/',views.goodbye,name = 'goodbye'),
]