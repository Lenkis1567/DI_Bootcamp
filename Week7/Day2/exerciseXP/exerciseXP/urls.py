"""
URL configuration for exerciseXP project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from work.views import DepartmentListAPIView, EmployeeListAPIView, DepartmentRetrieveAPIView, ProjectListAPIView, ProjectUpdateAPIView, ProjectDestroyAPIView, TaskViewSet, router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/departments/', DepartmentListAPIView.as_view(), name='deplist'),
    path('api/employees/', EmployeeListAPIView.as_view(), name='emplist'),
    path('api/departments/<int:pk>/', DepartmentRetrieveAPIView.as_view(), name='dept'),
    path('api/projects/', ProjectListAPIView.as_view(), name='proj'),
    path('api/projects/<int:pk>/', ProjectUpdateAPIView.as_view(), name='projects'),
    path('api/projects/<int:pk>/destr', ProjectDestroyAPIView.as_view(), name='pr_dest'),
    # path('api/task/<int:pk>/', TaskRetrieveAPIView.as_view(), name='task'),
    # path('api/task/<int:pk>/destr', TaskDestroyAPIView.as_view(), name='task_dest'),
    # path('api/tasks/', TaskListAPIView.as_view(), name='tasks'),
    # path('api/tasks/', TaskViewSet.as_view({'get': 'list'})),
    # path('api/tasks/<int:pk>/', TaskViewSet.as_view({'put': 'update'}))
    path('api/', include(router.urls), name='task')
    
]

