from django.contrib import admin

from tags.models import Tag


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = '__all__'
    search_fields = ('name', 'slug')
    list_editable = '__all__'
