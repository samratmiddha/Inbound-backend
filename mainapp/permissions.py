from rest_framework import permissions


class FullAccessPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        is_allowed = request.user.year == 3 or request.user.year == 4
        return is_allowed
