from rest_framework import permissions


class ProrfilePermission(permissions.BasePermission):

    def has_objects_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.userPro.id == request.user.id
