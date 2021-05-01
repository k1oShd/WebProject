from django.shortcuts import render
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated
from django.http.response import HttpResponse,JsonResponse
from api.models import Manufacturer,Category,Prodcut
from django.db.models import Count
# for Serialization
from rest_framework import viewsets, permissions
from .serializers import ProductSerializer, ManufacturerSerializer, CategorySerializer
# for CBV
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


# Create your views here.

#Basic Views

def check(request, username_, password_):
    user = authenticate(username=username_, password=password_)
    if user.is_authenticated:
        return HttpResponse('<h1>WEB Application is On-Line and operational...</h1>')
    else:
        return HttpResponse('<h1>PERMISSION DENIED</h1>')

def show_categories(request):
    categories = Category.objects.all()
    categories_json = (category.to_json() for category in categories)
    return JsonResponse(categories_json)

def show_category(request,category_id):
    categories = Category.objects.filter(pk=category_id)
    category_json = category.to_json()
    return JsonResponse(category_json)

def show_products(request,category_id):
    products = Product.objects.filter(ForeignKey=category_id)
    products_json = (product.to_json() for product in products)
    return JsonResponse(products_json)
    
def show_product(request, category_id, product_id):
    product = Product.objects.filter(pk=product_id)
    product_json = product.to_json()
    return JsonResponse(product_json)

# Serialization and CBV Part

class ProductView(viewsets.ModelViewSet):
    queryset = Prodcut.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ManufacturerView(viewsets.ModelViewSet):
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class CategoryView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class TestCategoryClassView(APIView):
        def get_object(self, pk):
            try:
                return Category.objects.get(pk=pk)
            except Category.DoesNotExist:
                raise Http404

        def get(self, request, pk, username_, password_, format=None):
            category = self.get_object(pk)
            serializer = CategorySerializer(category)
            return Response(serializer.data)

        def put(self, request, pk, format=None):
            category = self.get_object(pk)
            serializer = CategorySerializer(category, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        def delete(self, request, pk, format=None):
            category = self.get_object(pk)
            category.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)


# Authentication Part

class LogoutView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)