from django.contrib import admin
from .models import User, Team, Activity, Workout, Leaderboard
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

class UserAdmin(BaseUserAdmin):
    fieldsets = BaseUserAdmin.fieldsets + (
        (None, {'fields': ('team',)}),
    )
    add_fieldsets = BaseUserAdmin.add_fieldsets + (
        (None, {'fields': ('team',)}),
    )
    list_display = ('username', 'email', 'team', 'is_staff', 'is_superuser')
    search_fields = ('username', 'email')

admin.site.register(User, UserAdmin)
admin.site.register(Team)
admin.site.register(Activity)
admin.site.register(Workout)
admin.site.register(Leaderboard)
