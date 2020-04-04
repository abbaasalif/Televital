from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
    def has_object_permission(self, request, view,obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        elif request.user.is_doctor==True:
            return True

        else:
            return obj.id == request.user.id

class UpdateOwnVitals(permissions.BasePermission):
    """Allows users to update own status"""
    def has_object_permission(self, request, view, obj):
        """Check if the user is trying to update their own status"""
        if request.method in permissions.SAFE_METHODS:
            return True
        elif request.user.is_doctor==True:
            return True
        else:
            return obj.user_profile.id== request.user.id
