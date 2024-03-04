from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'username', 'age', 'can_be_contacted', 'can_data_be_shared', 'created_time']
        read_only_fields = ['created_time']
        extra_kwargs = {
            'password': {'write_only': True}  # Ensure password field is write-only
        }

