from django.core.exceptions import ValidationError
from rest_framework.permissions import BasePermission, IsAdminUser


class PermissionPolicyMixin:
    def check_permissions(self, request):
        try:
            handler = getattr(self, request.method.lower())
        except AttributeError:
            handler = None

        if handler and self.permission_classes_per_method and self.permission_classes_per_method.get(handler.__name__):
            self.permission_classes = self.permission_classes_per_method.get(handler.__name__)

        super().check_permissions(request)


class IsOwner(BasePermission):
    message = 'У вас нет доступа: Вы не Администратор или не владелец данной учетной записи'

    def has_object_permission(self, request, view, obj):
        if request.user.id == obj.id:
            return True

        elif obj.id is None and obj.is_staff:
            return True
        return False

