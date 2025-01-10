from rest_framework.views import Response, APIView
from .models import Fragrance, Price
from rest_framework.permissions import IsAuthenticated
from .serializers import FragrancePriceSerializer, FragranceSerializer
from rest_framework import status
from scraping.main import get_price
from django.utils import timezone

class FragranceView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        fragrances = Fragrance.objects.filter(user=self.request.user)
        today = timezone.now().date()
        for fragrance in fragrances:
            if not Price.objects.filter(fragrance=fragrance, date__date=today).exists():
                price = get_price(fragrance.website, fragrance.url)
                Price.objects.create(
                    fragrance=fragrance,
                    name=fragrance.website,
                    price=price,
                    date=timezone.now()
                )
        serializer = FragrancePriceSerializer(fragrances, many=True)
        print(serializer.data)
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
            today = timezone.now().date()
            if not Price.objects.filter(fragrance=fragrance, date__date=today).exists():
                price = get_price(fragrance.website, fragrance.url)
                Price.objects.create(
                    fragrance=fragrance,
                    name=fragrance.website,
                    price=price,
                    date=timezone.now()
                )
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

