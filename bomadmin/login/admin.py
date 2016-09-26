from django.contrib import admin
from models import UserProfile, UserProfileAdmin
#admin.site.register(UserProfile, UserProfileAdmin)
#class UserProfileInline(admin.StackedInline):
#    model = UserProfile
#    fk_name = 'user'
#    max_num = 1
#
#class UserProfileAdmin(UserAdmin):
#    inlines = [UserProfileInline,]
admin.site.register(UserProfile,UserProfileAdmin)
