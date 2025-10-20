from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('login/', views.login_view, name='login_view'),
    path('register/', views.register_view, name='register_view'),
    path('logout/', views.logout_view, name='logout_view'),
    path('profile/', views.profile_view, name='profile'),
]