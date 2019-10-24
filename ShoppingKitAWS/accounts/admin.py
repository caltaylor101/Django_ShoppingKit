from django.contrib import admin
from accounts.models import UserProfile
# Register your models here.
class UserProfileAdmin(admin.ModelAdmin): 
    list_display = ('user', 'user_info', 'city')

    #allows to add info from list display and change user_info's name.
    def user_info(self, obj): 
        return obj.description
    user_info.short_description = 'Information'

    #orders data in admin database
    def get_queryset(self, request):
        queryset = super(UserProfileAdmin, self).get_queryset(request)
        queryset = queryset.order_by('city')
        return queryset


    


admin.site.register(UserProfile, UserProfileAdmin)

admin.site.site_header= "Administration"


    