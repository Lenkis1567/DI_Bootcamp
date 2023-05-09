from django.shortcuts import render, redirect
from .models import Department, Employee, Project, Task
from .serializers import TaskSerializer, DepartmentSerializer, EmployeeSerializer, ProjectSerializer
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
from rest_framework.generics import GenericAPIView, ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework import mixins

class DepartmentListAPIView(mixins.CreateModelMixin, ListAPIView):
    serializer_class = DepartmentSerializer
    permission_classes = (IsAuthenticated,)
    def get_queryset(self):
        queryset = Department.objects.all()
        return queryset

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
class EmployeeListAPIView(mixins.CreateModelMixin, ListAPIView):
    serializer_class = EmployeeSerializer
    permission_classes = (IsAuthenticated,)
    def get_queryset(self):
        queryset = Employee.objects.all()
        return queryset

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
class DepartmentRetrieveAPIView(RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class ProjectListAPIView(mixins.CreateModelMixin, ListAPIView):
    serializer_class = ProjectSerializer
    permission_classes = (IsAuthenticated,)
    def get_queryset(self):
        queryset = Project.objects.all()
        return queryset

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ProjectUpdateAPIView(UpdateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()


class ProjectDestroyAPIView(DestroyAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()

class TaskRetrieveAPIView(mixins.CreateModelMixin, RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = TaskSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
    def get_queryset(self):
        queryset = Task.objects.all()
        return queryset

    
class TaskDestroyAPIView(DestroyAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = TaskSerializer

class TaskListAPIView(mixins.CreateModelMixin, ListAPIView):
    serializer_class = TaskSerializer
    permission_classes = (IsAuthenticated,)
    def get_queryset(self):
        queryset = Task.objects.all()
        return queryset

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
