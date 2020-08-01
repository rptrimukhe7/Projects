from django.urls import path
from demoapp import views

urlpatterns = [
    path('hello/', views.m1),
    path('stu/',views.stu),
    path('student/',views.Student_list),
    path('student/<int:pk>/',views.Student_detail),
]