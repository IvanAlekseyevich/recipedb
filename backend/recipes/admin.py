from django.contrib import admin

from recipes import models


class RecipeIngredientInline(admin.StackedInline):
    model = models.Recipe.ingredients.through
    extra = 0


class RecipeTagInline(admin.StackedInline):
    model = models.Recipe.tags.through
    extra = 1


@admin.register(models.Recipe)
class RecipeAdmin(admin.ModelAdmin):
    inlines = (RecipeIngredientInline, RecipeTagInline)
    list_display = ('name', 'author', 'pub_date')
    search_fields = ('author', 'name', 'tags')
    list_filter = ('author', 'name', 'tags')
    list_editable = ('name',)
    list_display_links = ('author',)


@admin.register(models.RecipeIngredient)
class RecipeIngredientAdmin(admin.ModelAdmin):
    list_display = ('id', 'recipe', 'ingredient', 'amount')
    search_fields = ('recipe', 'ingredient')
    list_editable = ('ingredient', 'amount')


@admin.register(models.RecipeTag)
class RecipeTagAdmin(admin.ModelAdmin):
    list_display = ('id', 'recipe', 'tag')
    search_fields = ('recipe', 'tag')
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
