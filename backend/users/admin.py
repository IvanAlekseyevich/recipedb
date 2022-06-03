from django.contrib import admin
from django.contrib.auth.models import Group

from users.models import Subscription, User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'first_name', 'last_name')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    list_editable = ('email', 'first_name', 'last_name')
    list_display_links = ('username',)


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'subscriber')
    search_fields = ('author', 'subscriber')


admin.site.unregister(Group)
