from rest_framework.permissions import BasePermission


class IsUser(BasePermission):
    message = "Вы не являетесь создателем привычки!"

    def has_permission(self, request, view):
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user
