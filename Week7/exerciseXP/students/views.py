from django.shortcuts import render, redirect
from .models import Student
from .serializers import StudentSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import (IsAdminUser,
                                        IsAuthenticated,
                                        AllowAny)
from rest_framework.status import (HTTP_200_OK,
                                   HTTP_201_CREATED,
                                   HTTP_202_ACCEPTED,
                                   HTTP_204_NO_CONTENT,
                                   HTTP_400_BAD_REQUEST)
# from rest_framework.generics import GenericAPIVIew, ListAPIView


class StudentView(APIView):
    
    def get(self, request, *args, **kwargs):

        pk = kwargs.get('pk')
        
        if pk:
            try:
                instance = Student.objects.get(id=pk)
                serializer = StudentSerializer(instance)
            except Student.DoesNotExist:
                return Response({"detail": "Student not found"}, status=HTTP_400_BAD_REQUEST)
        else:
            date_joined_param = request.GET.get('date_joined')
            if date_joined_param:
                queryset = Student.objects.filter(date_joined=date_joined_param)
                serializer = StudentSerializer(queryset, many=True)
            else:
                queryset = Student.objects.all()
                serializer = StudentSerializer(queryset, many=True)
        return Response(serializer.data, status=HTTP_200_OK)
    
    def post(self, request, *args, **kwargs):
        print("************************",request.data)
        serializer = StudentSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = HTTP_201_CREATED)
        
        return Response(serializer.errors, status = HTTP_400_BAD_REQUEST)
    
    def delete(self, request, *args, **kwargs):

        pk = kwargs.get('pk')
        
        if pk:
            try:
                post = Student.objects.get(id=pk)
                post.delete()
                return Response({"detail": "Student was deleted!"}, status=HTTP_204_NO_CONTENT)
            except Student.DoesNotExist:
                return Response({"detail": "Student not found"}, status=HTTP_400_BAD_REQUEST)

        else:
            return redirect('post-list')

    def put(self, request, *args, **kwargs):

        pk = kwargs.get('pk')

        if pk:
            try:
                post = Student.objects.get(id=pk)
                serializer = StudentSerializer(post, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data)
                
            except Student.DoesNotExist:
                return Response({"detail": "Student not found"}, status=HTTP_400_BAD_REQUEST)
        else:
           return Response({"detail": "Student wasn't found"}, status=HTTP_400_BAD_REQUEST) 

