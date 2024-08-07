from rest_framework import permissions


class IsOwner(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.user == view.get_object().user


class OrdinaryUser(permissions.BasePermission):
    def has_permission(self, request, view):
        print(view.get_object())
        print(view.get_object().is_published)
        return True
