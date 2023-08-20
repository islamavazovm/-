import datetime

from django.shortcuts import HttpResponse, render
from posts.models import Post, Product, Category



def main_view(request):
    if request.method == "GET":
        return render(request, 'layouts/index.html')

def posts_view(request):
    if request.method == "GET":
        posts = Post.objects.all()

        context_data = {
            'posts' : posts
        }

        return render(request, 'posts/posts.html', context=context_data)

def product_view(request):
    if request.method == 'GET':
        product = Product.objects.all()

        context_product = {
            'product' : product
        }
        return render(request, 'product/product.html', context=context_product)


def category_view(request):
    if request.method == 'GET':
        category = Category.objects.all()

        context_category = {
            'category' : category
        }
        return render(request, 'category/category.html', context=context_category)


