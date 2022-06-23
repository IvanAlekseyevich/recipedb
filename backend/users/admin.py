from django.contrib import admin
from django.contrib.auth.models import Group
from rest_framework.authtoken.models import TokenProxy
from users.models import Subscription, User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    list_filter = ('username', 'email')
    list_display_links = ('username',)
    fieldsets = (
        (None, {
            'fields': ('date_joined', 'username', 'email', 'first_name', 'last_name')
        }),
        ('Расширенные настройки', {
            'classes': ('collapse',),
            'fields': ('is_active', 'is_staff', 'is_superuser'),
        }),
    )
    readonly_fields = ('date_joined',)


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('author', 'subscriber')
    search_fields = ('author', 'subscriber')


admin.site.unregister(Group)
admin.site.unregister(TokenProxy)
