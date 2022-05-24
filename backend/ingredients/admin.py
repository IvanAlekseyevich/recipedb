from django.contrib import admin

from ingredients.models import Ingredient


@admin.register(Ingredient)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'measurement_unit',)
    search_fields = ('name',)
    list_editable = ('name', 'measurement_unit',)
