from django.contrib import admin
from accounts.models import UserProfile #import UserProfile class from accounts.models
# Register your models here.

#admin.site.site_header = 'Adminstration'


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user','user_info','city','website','phone')

    def user_info(self, obj):
        return obj.description

    user_info.short_description = 'Info'

    def get_queryset(self, request):
        queryset = super(UserProfileAdmin, self).get_queryset(request)
        queryset = queryset.order_by('-user') #for opposite you can put - in front of argument
        # you can specify multiple fields e.g., ('-user','phone','etc')
        return queryset



admin.site.register(UserProfile, UserProfileAdmin)
