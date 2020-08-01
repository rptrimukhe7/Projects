from demoapp.models import Student
from .serializers import StudentSerializers
from rest_framework import generics
from django.http import HttpResponse




def m1(request):
    return HttpResponse(" Hello Django")


# def stu(request):
#     data = Student.objects.all()
#     return render(request,'demoapp/s.html',{'data':data})



class StudentList(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers



class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers

