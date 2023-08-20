from django.contrib import admin
from posts.models import Post, Product, Category

admin.site.register(Post)
admin.site.register(Product)
admin.site.register(Category)