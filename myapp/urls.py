from django.urls import path
from . import views
from .views import Home

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('projects/<int:pk>/', views.ProjectDetail.as_view(), name='project-detail'),
    path('projects/<int:pk>/edit/', views.ProjectUpdate.as_view(), name='project-update'),
    path('projects/<int:pk>/delete/', views.ProjectDelete.as_view(), name='project-delete'),
    path('book-now/', views.create_C, name='create'),
]