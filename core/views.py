from rest_framework import generics, permissions, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework.views import APIView
from django.db.models import Q
from rest_framework.decorators import api_view, permission_classes
from .permissions import IsCustomAdmin

# Auth
class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer

# Sweet Views
class SweetListCreateView(generics.ListCreateAPIView):
    queryset = Sweet.objects.all()
    serializer_class = SweetSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        if not self.request.user.is_admin:
            raise PermissionDenied("Only admins can create sweets.")
        serializer.save()


class SweetSearchView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        sweet_id = request.query_params.get('q', '')
        try:
            sweet = Sweet.objects.get(pk=sweet_id)
            serializer = SweetSerializer(sweet)
            return Response(serializer.data)
        except Sweet.DoesNotExist:
            return Response({"error": "Sweet not found"}, status=404)



class SweetUpdateView(generics.UpdateAPIView):
    queryset = Sweet.objects.all()
    serializer_class = SweetSerializer
    permission_classes = [permissions.IsAuthenticated, IsCustomAdmin]
    http_method_names = ['put', 'patch']  # Enables PATCH for partial updates

    def get_serializer(self, *args, **kwargs):
        kwargs['partial'] = True  # Allow partial updates
        return super().get_serializer(*args, **kwargs)


class SweetDeleteView(generics.DestroyAPIView):
    queryset = Sweet.objects.all()
    serializer_class = SweetSerializer
    permission_classes = [permissions.IsAuthenticated, IsCustomAdmin]

class PurchaseSweetView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        try:
            sweet = Sweet.objects.get(pk=pk)
        except Sweet.DoesNotExist:
            return Response({"error": "Sweet not found"}, status=404)

        quantity = request.data.get('quantity', 1)
        try:
            quantity = int(quantity)
        except ValueError:
            return Response({"error": "Quantity must be an integer"}, status=400)

        if quantity <= 0:
            return Response({"error": "Quantity must be at least 1"}, status=400)

        if sweet.quantity < quantity:
            return Response({"error": f"Only {sweet.quantity} available. Cannot purchase {quantity}."}, status=400)

        sweet.quantity -= quantity
        sweet.save()

        Purchase.objects.create(user=request.user, sweet=sweet, quantity=quantity)

        return Response({"message": f"Successfully purchased {quantity} of {sweet.name}."})



class RestockSweetView(APIView):
    permission_classes = [permissions.IsAdminUser]

    def post(self, request, pk):
        sweet = Sweet.objects.get(pk=pk)
        sweet.quantity += 1
        sweet.save()
        return Response({"message": "Restocked successfully"})

class UserPurchaseListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        purchases = Purchase.objects.filter(user=request.user).select_related('sweet')
        serializer = PurchaseSerializer(purchases, many=True)
        return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_logged_in_user(request):
    user = request.user
    return Response({
        'username': user.username,
        'email': user.email,
        'is_admin': user.is_admin,
    })        