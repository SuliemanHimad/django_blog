from django.contrib import admin
from blog.models import Category,Post
# Register your models here.


class postAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Category)
admin.site.register(Post, postAdmin)