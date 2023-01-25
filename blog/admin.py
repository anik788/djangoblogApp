from django.contrib import admin
from blog.models import Post, Rating, Category


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'body', 'created_at', 'modified_at',)
    search_fields = ('title', 'body',)
    list_filter = ('rating__value',)
    raw_id_fields = ('categories',)
    list_per_page = 5


admin.site.register([Rating, Category])
