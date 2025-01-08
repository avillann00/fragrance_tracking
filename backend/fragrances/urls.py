from .views import FragranceView, DeleteFragranceView, SingleFragranceView
from django.urls import path

urlpatterns = [
    path('fragrances/', FragranceView.as_view(), name='fragrances'),
    path('fragrances/<int:pk>/', DeleteFragranceView.as_view(), name='delete-fragrance'),
    path('details/<int:pk>/', SingleFragranceView.as_view(), name='single-fragrance')
]
