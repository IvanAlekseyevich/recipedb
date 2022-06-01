from django.contrib import admin

from recipes.models import FavoriteRecipe, Recipe, ShoppingCart


class IngredientAmountInline(admin.StackedInline):
    model = Recipe.ingredients.through
    extra = 0


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    inlines = (IngredientAmountInline,)
    list_display = ('author', 'name', 'image', 'text', 'cooking_time', 'pub_date')
    search_fields = ('author', 'name', 'tags')
    list_filter = ('author', 'name', 'tags')
    list_editable = ('name', 'image', 'text', 'cooking_time')
    list_display_links = ('author',)


@admin.register(FavoriteRecipe)
class FavoriteAdmin(admin.ModelAdmin):
    list_display = ('user', 'recipe')
    search_fields = ('user',)


@admin.register(ShoppingCart)
class ShoppingAdmin(admin.ModelAdmin):
    list_display = ('user', 'recipe')
    search_fields = ('user',)
    list_editable = ('recipe',)
    list_display_links = ('user',)
