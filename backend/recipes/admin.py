from django.contrib import admin

from recipes import models


class RecipeIngredientInline(admin.StackedInline):
    model = models.Recipe.ingredients.through
    extra = 0


@admin.register(models.Recipe)
class RecipeAdmin(admin.ModelAdmin):
    inlines = (RecipeIngredientInline,)
    list_display = ('id', 'author', 'name', 'image', 'text', 'cooking_time', 'pub_date')
    search_fields = ('author', 'name', 'tags')
    list_filter = ('author', 'name', 'tags')
    list_editable = ('name', 'image', 'text', 'cooking_time')
    list_display_links = ('author',)


@admin.register(models.RecipeIngredient)
class RecipeIngredientAdmin(admin.ModelAdmin):
    list_display = ('id', 'ingredient', 'recipe', 'amount')
    search_fields = ('ingredient', 'recipe')
    list_editable = ('ingredient', 'amount')


@admin.register(models.RecipeTag)
class RecipeTagAdmin(admin.ModelAdmin):
    list_display = ('id', 'tag', 'recipe')
    search_fields = ('tag', 'recipe')
    list_editable = ('tag',)


@admin.register(models.FavoriteRecipe)
class FavoriteAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'recipe')
    search_fields = ('user',)
    list_editable = ('recipe',)


@admin.register(models.ShoppingCart)
class ShoppingAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'recipe')
    search_fields = ('user',)
    list_editable = ('recipe',)
