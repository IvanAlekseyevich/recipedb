from django.contrib import admin

from ingredients.models import Ingredient


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'amount', 'measurement_unit')
    search_fields = ('name',)
    list_editable = ('name', 'amount', 'measurement_unit')
