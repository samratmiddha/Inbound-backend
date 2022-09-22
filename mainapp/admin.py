from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.admin import UserAdmin 
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth import get_user_model
from mainapp.models import *


# class UserAdmin(BaseUserAdmin):
#     form =UserChangeForm
#     fieldsets = (
#         (None,{'fields':('username','password')}),
#         (('Personal info'),{'fields':('name','enrolment_number','email','year','role')}),
#         (('Permissions'),{'fields':('is_active','is_staff','is_superuser','groups','user_permissions')}),
#     )
#     add_fieldsets = (
#         (None,{
#             'classes':('wide',),
#             'fields':('username','password'),
#         }),
#     )
#     list_display = ['username','enrolment_number','email','year','role','is_staff']
#     search_fields=('username','name')
#     ordering=('name',)
# Register your models here.
admin.site.register(Candidate)
 

admin.site.register(InfoToConvey)

admin.site.register(Interview_Panel)

admin.site.register(Question_Status)

admin.site.register(Question)

admin.site.register(Round_Info)

admin.site.register(Round)

admin.site.register(Season)

admin.site.register(Section)

admin.site.register(Sectional_Marks)


admin.site.register(User,UserAdmin)
