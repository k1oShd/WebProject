from django.urls import path,re_path
from api.views import check
from api.views import show_categories,show_category,show_products#,show_product
from rest_framework_jwt.views import obtain_jwt_token
# NEw Views
from .views import ProductView, ManufacturerView, CategoryView,TestCategoryClassView, LogoutView

product_list = ProductView.as_view({
    'get': 'list'
})

manufacturer_list = ManufacturerView.as_view({
    'get': 'list'
})

category_list = CategoryView.as_view({
    'get': 'list'
})

urlpatterns = [
    path('login/', obtain_jwt_token),   
    path('logout/', LogoutView.as_view(), name='auth_logout'),
    path('categories/', show_categories),
    path('companies/<int:category_id>/', show_category),
    path('companies/<int:category_id>/prodcuts/', show_products),
    path('companies/<int:category_id>/prodcuts/<int:product_id/>', show_product),
    path('check/<str:username_>/<str:password_>', check),
    path('productsSer/', product_list, name='product_list'),
    path('manufacturerSer/', manufacturer_list, name='manufacturer_list'),
    path('categoriesSer/', category_list, name='category_list'),
    path('testshowcat/<int:pk>/', TestCategoryClassView.as_view())
]