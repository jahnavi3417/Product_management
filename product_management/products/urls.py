from django.urls import path
from .views import ShowAllProducts
from products import views

urlpatterns=[
    path('',views.ShowAllProducts,name='ShowProducts'),
    path('product/<int:pk>',views.productDetail, name='productDetail'),
    path('byproducts/<int:pk>',views.Byproduct,name='byproduct'),
    path('addProduct',views.addProduct, name='addproduct'),
    path('updateproduct/<int:pk>',views.updateProduct,name='updateProduct'),
    path('deleteproduct/<int:pk>',views.deleteProduct ,name='deleteproduct'),
    path('search/',views.SearchBar, name='search'),
    path('continue',views.Address,name='continue'),
    path('user/<int:pk>',views.user,name='User'),
]

#static ,dynamic,cms:content management system,or midd levelprojects,erp