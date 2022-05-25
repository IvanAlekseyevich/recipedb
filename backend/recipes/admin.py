from django.contrib import admin

from recipes.models import Recipe


@admin.register(Recipe)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('author', 'subscriber',)
    search_fields = ('author', 'subscriber',)


