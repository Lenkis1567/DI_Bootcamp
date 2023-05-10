from rest_framework import permissions
from .models import Department

class IsLLL(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user.username !='LLL':
            return False
        return True


class IsDepartmentAdmin(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.user =='Department.admin':
            return True
        return False