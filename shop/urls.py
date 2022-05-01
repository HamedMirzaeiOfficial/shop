from django.urls import path
from shop import views

app_name = 'shop'

urlpatterns = [
    path('product_list/', views.ProductListView.as_view(), name='product_list'),
    path('product_list/<slug:slug>/', views.ProductListView.as_view(), name='product_list_by_category'),
    path('<int:id>/<slug:slug>/', views.ProductDetailView.as_view(), name='product_detail'),
    path('search/', views.SearchResultsView.as_view(), name='search_results'),

]
