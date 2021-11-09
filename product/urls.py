from django.urls import path
from product.views import *

app_name = 'product'

urlpatterns = [
    path('',ProductPageView.as_view(),name='products'),
    path('add-product/',AddProductPageView.as_view(),name='add-product'),
    path('sale-products/',SaleProductPageView.as_view(),name='sale-products'),
    path('<str:model_slug>/<str:marka_slug>/<str:parent_detail_slug>/<str:subparent_detail_slug>/<str:child_detail_slug>/',FilteredProducts.as_view(),name='filtered-products'),
]