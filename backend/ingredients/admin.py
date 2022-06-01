from django.contrib import admin

from ingredients.models import Ingredient, IngredientAmount


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'measurement_unit')
    search_fields = ('name',)
    list_editable = ('name', 'measurement_unit')
    list_filter = ('measurement_unit',)
    ordering = ('name',)


@admin.register(IngredientAmount)
class IngredientAmount(admin.ModelAdmin):
    list_display = ('id', 'ingredient', 'amount')
    search_fields = ('ingredient',)
    list_editable = ('ingredient', 'amount')
    ordering = ('ingredient',)