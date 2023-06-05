from django.contrib.auth.models import get_user_model
from rest_framework import serializers

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'profile']
    def create(self, validated_data):
      password = validated_data.pop('password')
      user = User(**validated_data)
      user.set_password(password)
      user.save()
      return user