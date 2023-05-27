from django.contrib import admin

from .models import Category, Post, Location

admin.site.empty_value_display = 'Не задано'


class PostAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'text',
        'pub_date',
        'author',
        'location',
        'category',
        'is_published',
        'created_at',
    )
    list_editable = (
        'is_published',
        'category',
        'text',
    )
    search_fields = ('title',)
    list_fields = ('is_published',)
    list_filter = ('created_at',)
    list_display_links = ('title',)


admin.site.register(Category)
admin.site.register(Post, PostAdmin)
admin.site.register(Location)
