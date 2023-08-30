import datetime

from django.shortcuts import HttpResponse, render
from posts.models import Post, Product, Category, Review



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

def product_detail_view(request, id):
    if request.method == 'GET':
        product = Product.objects.get(id=id)

    context_data = {
        'product' : product
    }
    return render(request, 'product/detail.html',context=context_data)

def post_detail_view(request, id):
    if request.method == 'GET':
        post = Post.objects.get(id=id)

    context_data = {
        'post': post
    }

    return render(request, 'posts/detail.html', context=context_data)

def review_view(request):
    if request.method == 'GET':
        review = Review.objects.all()

    context_data = {
        'review': review
    }
    return render(request, 'product/review.html', context=context_data)

