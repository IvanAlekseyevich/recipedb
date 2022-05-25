from django.contrib import admin

from recipes.models import Favorite, Recipe, ShoppingCart


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('author', 'name')
    search_fields = ('author', 'name', 'tags')
    list_filter = ('author', 'name', 'tags')
    list_editable = '__all__'


@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    list_display = '__all__'
    search_fields = 'user'


@admin.register(ShoppingCart)
class ShoppingAdmin(admin.ModelAdmin):
    list_display = '__all__'
    search_fields = 'user'
    list_editable = '__all__'
