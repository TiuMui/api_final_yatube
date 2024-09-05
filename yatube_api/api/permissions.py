from rest_framework.permissions import BasePermission, SAFE_METHODS


class ReadOrAuthOrAuthorPermission(BasePermission):

    def has_permission(self, request, view):
        return bool(
            request.method in SAFE_METHODS
            or request.user and request.user.is_authenticated
        )

    def has_object_permission(self, request, view, obj):
        return bool(
            request.method in SAFE_METHODS or obj.author == request.user
        )
