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
    list_display = ('id', 'name', 'measurement_unit')
    search_fields = ('name',)
    list_filter = ('name',)
    list_editable = ('name', 'measurement_unit')
    ordering = ('name',)


@admin.register(models.Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'color', 'slug')
    search_fields = ('name', 'slug')
    list_editable = ('name', 'color', 'slug')
    ordering = ('name',)


@admin.register(models.Recipe)
class RecipeAdmin(admin.ModelAdmin):
    def favorite(self, obj):
        return obj.favorite.count()

    inlines = (RecipeIngredientInline, RecipeTagInline)
    list_display = ('name', 'author', 'favorite', 'pub_date')
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
