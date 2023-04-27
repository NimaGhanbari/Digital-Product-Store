from django.contrib import admin
from django.urls import path,include
from products.views import (ProductListView,ProductDetailView,CategorylistView,
                            CategoryDetailView,FileListView,FileDetailView,
                            )

urlpatterns = [
    path('',ProductListView.as_view(), name='products-list'),
    path('<int:pk>/',ProductDetailView.as_view(), name='products-detail'),
    path('category/',CategorylistView.as_view(),name ='categories-list'),
    path('category/<int:pk>/',CategoryDetailView.as_view(),name ='categories-Detail'),
    path('file/<int:product_pk>/',FileListView.as_view(),name= 'File-list'),
    path('file/<int:product_pk>/<int:pk>/',FileDetailView.as_view(),name= 'File-Detail'),
]