from rest_framework import serializers
from .models import User , UserManager
import bcrypt

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['email', 'username', 'age', 'can_be_contacted', 'can_data_be_shared', 'created_time', 'is_active', 'password']

    from rest_framework import serializers
    from .models import User
    from django.contrib.auth import get_user_model

    class UserSerializer(serializers.ModelSerializer):
        password = serializers.CharField(write_only=True)

        class Meta:
            model = User
            fields = ['email', 'username', 'age', 'can_be_contacted', 'can_data_be_shared', 'created_time', 'is_active',
                      'password']

        def create(self, validated_data):
            # Extracting data from validated_data
            email = validated_data.get('email')
            username = validated_data.get('username')
            age = validated_data.get('age')
            can_be_contacted = validated_data.get('can_be_contacted')
            can_data_be_shared = validated_data.get('can_data_be_shared')
            created_time = validated_data.get('created_time')
            is_active = validated_data.get('is_active')
            password = validated_data.get('password')

            # Creating the user
            manage = UserManager()
            manage.create_user(email, username, age, can_be_contacted, can_data_be_shared, created_time, is_active, password)

