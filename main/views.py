from django.shortcuts import render
from django.views import generic

from . import models

def index(request):
    return render(request, "index.html")

class Combinations(generic.ListView):
    template_name = "combinations.html"
    context_object_name = "combinations"
    model = models.Combination

class CombinationDetail(generic.DetailView):
    template_name = "combination-detail.html"
    context_object_name = "combination"
    model = models.Combination

class Categories(generic.ListView):
    template_name = "categories.html"
    context_object_name = "categories"
    model = models.Category

class CategoryDetail(generic.DetailView):
    template_name = "category-detail.html"
    context_object_name = "category"
    model = models.Category

class Products(generic.ListView):
    template_name = "products.html"
    context_object_name = "products"
    model = models.Product

class ProductDetail(generic.DetailView):
    template_name = "product-detail.html"
    context_object_name = "product"
    model = models.Product

def Http501(request):
    return render(request, "501.html", status=501)
