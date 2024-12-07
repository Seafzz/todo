from django.urls import path, include
from . import views

urlpatterns = [
    # Admin URLs path
    path('custom_admin/dashboard/', views.admin_dashboard_view, name='admin_dashboard'), 

    path('', views.home, name='home'),
    path('tasks/', views.task_list, name='task_list'),
    path('create/', views.create_task, name='create_task'),
    path('edit/<int:pk>/', views.edit_task, name='edit_task'),
    path('delete/<int:pk>/', views.delete_task, name='delete_task'),
    path('detail/<int:pk>/', views.task_detail, name='task_detail'),
    path('profile/', views.view_profile, name='view_profile'),
    path('profile/edit/', views.update_profile, name='update_profile'),
    path('signup/', views.signup, name='signup'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('logout/', views.logout_view, name='logout'),
    path('tasks/<int:pk>/toggle_complete/',
         views.toggle_task_complete, name='toggle_task_complete'),
]
