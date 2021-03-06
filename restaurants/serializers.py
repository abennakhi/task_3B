from rest_framework import serializers
from .models import Restaurant


class RestaurantListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ['owner', 'name', 'description',
                  'opening_time', 'closing_time']
