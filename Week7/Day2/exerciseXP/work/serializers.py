from rest_framework import serializers
from .models import Department, Employee, Project, Task


class TaskSerializer(serializers.ModelSerializer):
    id = serializers.HyperlinkedIdentityField(view_name='task-detail')
    class Meta:
        model = Task
        fields = '__all__'

class DepartmentSerializer(serializers.ModelSerializer):
    id = serializers.HyperlinkedIdentityField(view_name='dept')
    class Meta:
        model = Department
        fields = '__all__'

class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employee
        fields = '__all__'

class ProjectSerializer(serializers.ModelSerializer):
    name = serializers.HyperlinkedIdentityField(view_name='projects')

    class Meta:
        model = Project
        fields = '__all__'
      