from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Product
from .serializers import ProductSerializer
from rest_framework.authtoken.models import Token
# Create your views here.

class IsProductCreator(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner_token == str(Token.objects.get(user=request.user))
    
class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.BasePermission, permissions.IsAuthenticated]
    def perform_create(self, serializer):
        token, created = Token.objects.get_or_create(user=self.request.user)
        serializer.save(owner_token=token)

class ProductRetriveUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.BasePermission, permissions.IsAuthenticatedOrReadOnly, IsProductCreator]
    def perform_update(self, serializer):
        serializer.save(created_by=self.request.user)