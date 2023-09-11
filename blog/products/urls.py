from django.urls import path
from .views import ProductListCreateView, ProductRetriveUpdateDelete

urlpatterns = [
    path('', ProductListCreateView.as_view()),
    path('<int:pk>', ProductRetriveUpdateDelete.as_view())
]