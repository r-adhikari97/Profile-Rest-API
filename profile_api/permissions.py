from rest_framework import permissions

class UpdateOwProfile(permissions.BasePermission):
    """ Allow Users to Edit their own profile """

    def HasObjectPermission (self,request, view, obj):
        """  Check User trying to edit profile """

        # HTTP Get : Safe Method
        if request.method in permissions.SAFE_METHODS:
            return True

        # Http  DELETE, PUT : Not Safe Method
        return obj.id == request.user.id

