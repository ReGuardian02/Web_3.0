from django.contrib import admin
from .models import Post, Comment, Feedback, Tag, Product, Chat


class PostAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'text',
        'pub_date',
        'author'
    )
    search_fields = ('text',)
    list_filter = ('pub_date',)
    empty_value_display = '-пусто-'

class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'post',
        'author',
        'text'
    )

admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Feedback)
admin.site.register(Tag)
admin.site.register(Product)
admin.site.register(Chat)