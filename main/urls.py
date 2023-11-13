from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('combinations/', views.Combinations.as_view(), name="combinations"),
    path('combinations/<int:pk>/', views.CombinationDetail.as_view(), name="combination_detail"),
    path('categories/', views.Categories.as_view(), name="categories"),
    path('categories/<int:pk>/', views.CategoryDetail.as_view(), name="category_detail"),
    path('products/', views.Products.as_view(), name="products"),
    path('products/<int:pk>/', views.ProductDetail.as_view(), name="product_detail"),
    path('search/', views.Http501, name="search")
]
