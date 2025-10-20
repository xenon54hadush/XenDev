from django.urls import path
from .views import AdminHome, Details, Orders, permission_denied_view, create_project
from . import views

urlpatterns = [
    path('administration/', AdminHome.as_view(), name='admin_home'),
    path('details/<int:pk>/', Details.as_view(), name='details'),
    path('orders/', Orders.as_view(), name='orders'),
    path('create-post/', views.create_post, name='create-post'),
    path('create-project/', create_project, name='create-project'),
    path('update-post/<int:post_id>/', views.update_post, name='update-post'),
    path('delete-post/<int:post_id>/', views.delete_post, name='delete-post'),
    path('permission-denied/', permission_denied_view, name='permission_denied'),
]