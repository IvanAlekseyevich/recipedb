from django.contrib import admin

from users.models import Subscription, User


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = '__all__'
    search_fields = '__all__'


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = '__all__'
    search_fields = ('username', 'email')
    list_editable = '__all__'
