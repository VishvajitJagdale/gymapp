from django.urls import path
from . import views

urlpatterns = [
    path('', views.member_list, name='member_list'),
    path('create/', views.member_create, name='member_create'),
    path('update/<int:id>/', views.member_update, name='member_update'),
    path('delete/<int:id>/', views.member_delete, name='member_delete'),
    path('workout-plan/', views.workout_plan, name='workout_plan'),
    path('diet-plan/', views.diet_plan, name='diet_plan'),
]
