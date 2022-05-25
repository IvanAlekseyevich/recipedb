from django.contrib import admin

from ingredients.models import Ingredient


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = '__all__'
    search_fields = 'name'
    list_editable = '__all__'
    list_filter = 'name'
