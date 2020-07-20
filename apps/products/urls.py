from django.urls import path

from apps.products.views import (
    CategoryDetailView,
    CategoryListView,
    ProductDetailView,
    ProductListView
)


urlpatterns = [
    path('categories', CategoryListView.as_view(), name='categories-list'),
    path('categories/<int:pk>', CategoryDetailView.as_view(),
         name='categories-detail'),
    path('products', ProductListView().as_view(), name='products-list'),
    path('products/<int:pk>', ProductDetailView().as_view(),
         name='products-detail')
]
