from rest_framework import serializers
from .models import *
from django.contrib.auth import get_user_model

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['username', 'password', 'first_name', 'last_name', 'email', 'is_admin']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = get_user_model().objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', ''),
            email=validated_data.get('email', ''),
            is_admin=validated_data.get('is_admin', False)
        )
        return user


class SweetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sweet
        fields = '__all__'

class PurchaseSerializer(serializers.ModelSerializer):
    sweet = SweetSerializer()

    class Meta:
        model = Purchase
        fields = ['id', 'sweet', 'quantity', 'purchased_at']