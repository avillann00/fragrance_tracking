from rest_framework import serializers
from .models import Fragrance, Price

class FragranceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fragrance
        fields = '__all__'
        extra_kwargs = {'user': {'read_only': True}}


class PriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Price
        fields = '__all__'

class FragrancePriceSerializer(serializers.ModelSerializer):
    prices = PriceSerializer(many=True, read_only=True)

    class Meta:
        model = Fragrance
        fields = ['id', 'house', 'name', 'notes', 'website', 'url', 'user', 'prices']
