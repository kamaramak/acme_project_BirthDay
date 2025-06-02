from django.contrib import admin

from .models import Birthday, Tag


@admin.register(Birthday)
class BirthdayAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'first_name',
        'last_name',
        'birthday',
        'author'
    )
    list_display_links = (
        'first_name',
        'last_name',
        'birthday',
    )
    search_fields = (
        'first_name',
        'last_name',
    )
    list_editable = (
        'author',
    )


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('tag',)
    search_fields = ('tag',)
