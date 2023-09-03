from django.contrib import admin
from post.models import Post


# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ["id", "author", "title", "content"]

    list_filter = ["author"]


admin.site.register(Post, PostAdmin)
