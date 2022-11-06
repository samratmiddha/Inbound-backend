from rest_framework import permissions
from rest_framework.permissions import SAFE_METHODS
from datetime import date


class FullAccessSectionalMarksPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        is_allowed = request.user.year >2
        return is_allowed
    
    def has_object_permission(self,request,view,obj):
        if request.user.year==3:
            todays_date= date.today()
            current_year=todays_date.year
            return obj.section.round.season.session < current_year-1

        elif request.user.year==4:
            return True

        else :
            return False

    


class FullAccessQuestionMarksPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        is_allowed = request.user.year >2
        return is_allowed
    
    def has_object_permission(self,request,view,obj):
        if request.user.year==3:
            todays_date= date.today()
            current_year=todays_date.year
            return obj.question.section.round.season.session < current_year-1

        elif request.user.year==4:
            return True

        else :
            return False
class FullAccessRoundMarksPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        is_allowed = request.user.year >2
        return is_allowed
    
    def has_object_permission(self,request,obj):
        print('hii')
        if request.user.year==3:
            todays_date= date.today()
            current_year=todays_date.year
            return obj.round.season.session < current_year-1

        elif request.user.year==4:
            return True

        else :
            return False
    
    
class FullAccessPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        is_allowed = request.user.year >2
        return is_allowed
    


class ReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS
