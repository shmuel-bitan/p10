from rest_framework import serializers
from .models import User
import bcrypt

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['email', 'username', 'age', 'can_be_contacted', 'can_data_be_shared', 'created_time', 'is_active', 'password']

    def create(self, validated_data):
        password = validated_data.pop('password')
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        user = User(**validated_data)
        User.create_user(**validated_data, password=hashed_password)
        return user