from rest_framework import permissions


class IsAuthorOrStaffOrReadOnlyPermission(permissions.BasePermission):
    """Используется для создания, просмотра и изменения рецепта."""

    def has_permission(self, request, view):
        return (request.method in permissions.SAFE_METHODS
                or request.user.is_authenticated)

    def has_object_permission(self, request, view, obj):
        return (request.method in permissions.SAFE_METHODS
                or request.method == 'POST' and request.user.is_authenticated
                or obj.author == request.user
                or request.user.is_superuser)


class ReadOnlyPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.method in permissions.SAFE_METHODS
