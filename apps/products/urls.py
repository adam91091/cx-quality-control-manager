from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('', views.ProductListView.as_view(), name='products-list'),
    path('new/', views.ProductCreateView.as_view(), name='product-new'),
    path('detail/<int:pk>', views.ProductDetailView.as_view(), name='product-detail'),
    path('update/<int:pk>', views.ProductUpdateView.as_view(), name='product-update'),
    path('delete/<int:pk>', views.ProductDeleteView.as_view(), name='product-delete'),
    path('specification-issue/<int:pk>', views.SpecificationIssueFormView.as_view(), name='specification-issue'),
    path('specification-issue-confirm/<int:pk>',
         views.SpecificationIssueConfirmView.as_view(), name='specification-issue-confirm'),
    path('specification-pdf-render/<int:pk>', views.SpecificationPdfRenderView.as_view(),
         name='specification-pdf-render'),
]
