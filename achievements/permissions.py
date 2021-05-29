from rest_framework import permissions

class IsOwner(permissions.BasePermission):
    message="Not an owner"

    def has_object_permission(self, request, view, obj):
        print('IsOwner has_object_permission')
        print(request.user)
        return request.user == obj.owner
