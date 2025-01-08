from rest_framework import serializers
from rest_framework.views import Response, APIView
from .models import Fragrance, Price
from rest_framework.permissions import IsAuthenticated
from .serializers import FragrancePriceSerializer, FragranceSerializer
from rest_framework import status

class FragranceView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        fragrances = Fragrance.objects.filter(user=self.request.user)
        serializer = FragrancePriceSerializer(fragrances, many=True)
        return Response(serializer.data)

    def post(self, request):
        print(request.data)
        serializer = FragranceSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save(user=self.request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SingleFragranceView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        try:
            fragrance = Fragrance.objects.get(pk=pk, user=self.request.user)
            serializer = FragrancePriceSerializer(fragrance)
            return Response(serializer.data)
        except Fragrance.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

class DeleteFragranceView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, pk):
        try:
            fragrance = Fragrance.objects.get(pk=pk, user=self.request.user)
            fragrance.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Fragrance.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

