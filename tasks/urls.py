from django.urls import path
from . import views

urlpatterns =[
    path('', views.task_list, name='task_list'),
    path('create/', views.create_task, name='create_task'),
    path('edit/<int:pk>/', views.edit_task, name='edit_task'),
    path('delete/<int:pk>/', views.delete_task, name='delete_task'),
    path('detail/<int:pk>/', views.task_detail, name='task_detail'),
    path('profile/', views.view_profile, name='profile'),
    path('profile/edit/', views.update_profile, name='update_profile'),
]