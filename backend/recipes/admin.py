from django.contrib import admin
from recipes import models


class RecipeIngredientInline(admin.StackedInline):
    model = models.Recipe.ingredients.through
    extra = 0
    min_num = 1


class RecipeTagInline(admin.StackedInline):
    model = models.Recipe.tags.through
    extra = 0
    min_num = 1


@admin.register(models.Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ('name', 'measurement_unit')
    search_fields = ('name',)
    ordering = ('name',)


@admin.register(models.Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'color', 'slug')
    search_fields = ('name', 'slug')
    ordering = ('name',)


@admin.register(models.Recipe)
class RecipeAdmin(admin.ModelAdmin):
    def favorite(self, obj):
        return obj.favorite.count()

    inlines = (RecipeIngredientInline, RecipeTagInline)
    list_display = ('name', 'author', 'favorite', 'pub_date')
    search_fields = ('author', 'name', 'tags')
    list_display_links = ('author',)


@admin.register(models.RecipeIngredient)
class RecipeIngredientAdmin(admin.ModelAdmin):
    list_display = ('recipe', 'ingredient', 'amount')
    search_fields = ('recipe', 'ingredient')


@admin.register(models.RecipeTag)
class RecipeTagAdmin(admin.ModelAdmin):
    list_display = ('recipe', 'tag')
    search_fields = ('recipe', 'tag')


@admin.register(models.FavoriteRecipe)
class FavoriteAdmin(admin.ModelAdmin):
    list_display = ('user', 'recipe')
    search_fields = ('user',)


@admin.register(models.ShoppingCart)
class ShoppingAdmin(admin.ModelAdmin):
    list_display = ('user', 'recipe')
    search_fields = ('user',)
