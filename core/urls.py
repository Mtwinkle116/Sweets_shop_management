from django.urls import path
from .views import *

urlpatterns = [
    path('auth/register/', RegisterView.as_view(), name='register'),
    path('auth/me/', get_logged_in_user, name='me'),
    
    path('sweets/', SweetListCreateView.as_view(), name='sweet-list-create'),
    path('sweets/search/', SweetSearchView.as_view(), name='sweet-search'),
    
    path('sweets/<int:pk>/', SweetUpdateView.as_view(), name='sweet-update'),
    path('sweets/<int:pk>/delete/', SweetDeleteView.as_view(), name='sweet-delete'),
    path('sweets/<int:pk>/purchase/', PurchaseSweetView.as_view(), name='purchase-sweet'),
    path('sweets/<int:pk>/restock/', RestockSweetView.as_view(), name='restock-sweet'),

    path('user/purchases/', UserPurchaseListView.as_view(), name='user-purchases'),
]
