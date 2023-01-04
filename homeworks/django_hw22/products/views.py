from unicodedata import category

from django.shortcuts import render, redirect, get_object_or_404
from django.core.exceptions import PermissionDenied
from .models import Product, Category, CategoryProduct
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import PictureForm


def add_product(request):
    if request.user.is_authenticated:
        if request.method == "GET":
            categories = Category.objects.all()
            return render(request, "products/add.html", {"categories":categories})
        else:
            product = Product()
            product.title = request.POST.get("title")
            product.description = request.POST.get("description")
            product.user = request.user
            product.save()
            return redirect("/")
    else:
        return redirect("/")


def edit_product(request, id):
    if request.user.is_authenticated:
        product = Product.objects.get(id=id)
        categories = Category.objects.all()
        product_categories = CategoryProduct.objects.filter(product_id=product.id)
        return render(request, "products/add.html", {
            "product": product,
            "product_categories": product_categories,
            "categories": categories
        })
    else:
        raise PermissionDenied


def update_product(request, id):
    if request.user.is_authenticated:
        product = Product.objects.get(id=id)
        product.title = request.POST.get("title")
        product.description = request.POST.get("description")
        product.save()
        CategoryProduct.objects.filter(product_id=product.id).delete()
        for category in request.POST.getlist('categories', []):
            category_product = CategoryProduct()
            category_product.product = product
            category_product.category = Category.objects.get(id=int(category))
            category_product.save()
        return redirect("/")


def add_category(request):
    if request.user.is_authenticated:
        if request.method == "GET":
            return render(request, "products/category/add.html")
        else:
            category = Category()
            category.title = request.POST.get("title")
            category.save()
            return redirect("/")


def edit_category(request, id):
    if request.user.is_authenticated:
        category = Category.objects.get(id=id)
        products = Product.objects.all()
        category_product = CategoryProduct.objects.filter(category_id=category.id)
        return render(request, "products/category/add.html", {
            "category": category,
            "products": products,
            'category_product': category_product
        })
    else:
        raise PermissionDenied


def update_category(request, id):
    if request.user.is_authenticated:
        category = Category.objects.get(id=id)
        category.title = request.POST.get('title')
        category.save()
        CategoryProduct.objects.filter(category_id=category.id).delete()
        for product in request.POST.getlist('products', []):
            category_product = CategoryProduct()
            category_product.product = Product.objects.get(id=int(product))
            category_product.category = category
            category_product.save()
        return redirect('/')


def product_details(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, "products/details.html", {"product": product})


def upload_picture(request):
    if request.method == 'POST':
        form = PictureForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
    else:
        form = PictureForm
    return render(request, 'picture.html', {'form':form})