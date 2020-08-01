from django.urls import path
from demoapp import views

urlpatterns = [
    path('hey/', views.m1),
    # path('stu/',views.stu),
    path('student/', views.StudentList.as_view()),
    path('student/<int:pk>/', views.StudentDetail.as_view()),
    
    
]