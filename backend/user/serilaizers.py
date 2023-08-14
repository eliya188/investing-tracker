from rest_framework import serializers
from .models import Profile
from django.contrib.auth.models import User

class ProfileSerializers(serializers.ModelSerializer):
    password1 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["username", 'password', 'password1', 'email']

    def validate(self, data):
        """
        Custom validation to check if password and password1 match.
        """
        password = data.get('password')
        password1 = data.get('password1')

        if password != password1:
            raise serializers.ValidationError("Passwords do not match.")

        return data
    
    def create(self, validated_data):
        username = validated_data.get('username')
        password = validated_data.get('password')
        email = validated_data.get('email')

        user = User.objects.create_user(username=username, password=password, email=email)

        profile = Profile(user=user)
        profile.save()
        return user

