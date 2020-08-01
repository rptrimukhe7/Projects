from django.shortcuts import render
from django.http import HttpResponse
from demoapp.models import Student
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import StudentSerializers
from rest_framework import status
# Create your views here.
def m1(request):
    return HttpResponse(" Hello Django")


def stu(request):
    data = Student.objects.all()
    return render(request,'demoapp/s.html',{'data':data})

@api_view(['GET','POST'])
def Student_list(request):
    if request.method =='GET':
        obj = Student.objects.all()
        serializer = StudentSerializers(obj, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = StudentSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)        

# @api_view(['GET'])
# def Student_detail(request,pk):
#     try:
#         obj=Student.objects.get(id =pk)
#     except Student.DeoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#     serializer=StudentSerializers(obj)
#     return Response(serializer.data)        
    

@api_view(['GET','PUT'])
def Student_detail(request,pk):
    try:
        obj=Student.objects.get(id=pk)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer=StudentSerializers(obj)
        return Response(serializer.data)   
    elif request.method == 'PUT':
        serializer=StudentSerializers(obj,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.error,status=status.HTTP_404_BAD_REQUEST)             


    
    
    
    
    