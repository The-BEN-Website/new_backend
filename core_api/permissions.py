from rest_framework import permissions


class Pub(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        allowed_roles = ['ICT', 'PUBLICATION']
        if request.method in permissions.SAFE_METHODS:
            return True

        return request.user.role in allowed_roles
