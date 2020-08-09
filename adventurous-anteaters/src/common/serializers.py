from rest_framework import serializers

from .models import User


class UserSerializer(serializers.ModelSerializer):

    # login = serializers.CharField(max_length=100)
    # password = serializers.CharField(max_length=100)
    # first_name = serializers.CharField(allow_blank=True, max_length=100)
    # last_name = serializers.CharField(allow_blank=True, max_length=100)

    class Meta:
        model = User
        fields = ['login', 'password', 'first_name', 'last_name', 'created_at', 'updated_at']

    # def create(self, validated_data):
    #     """
    #     Create and return a new `User` instance, given the validated data.
    #     """
    #     return User.objects.create(**validated_data)

    # def update(self, instance, validated_data):
    #     """
    #     Update and return an existing `User` instance, given the validated data.
    #     """
    #     instance.login = validated_data.get('login', instance.login)
    #     instance.password = validated_data.get('password', instance.password)
    #     instance.first_name = validated_data.get('first_name', instance.first_name)
    #     instance.last_name = validated_data.get('last_name', instance.last_name)
    #     instance.save()
    #     return instance
