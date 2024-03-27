from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import AccessToken
from .models import User
from .serializers import UserSerializer
import bcrypt


class UserListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class LoginView(APIView):
    def post(self, request):
        # Get the email and password from the request data
        email = request.data.get('email')
        password = request.data.get('password')

        # Check if both email and password are provided
        if not email or not password:
            return Response({'error': 'Email and password are required'}, status=status.HTTP_400_BAD_REQUEST)

        # Try to get the user from the database using the provided email
        user = User.objects.filter(email=email).first()
        raw_password = password.encode('utf-8')
        pswd = user.password

        print(raw_password)
        # Check if the user exists and the password is correct
        if user is not None and bcrypt.checkpw(raw_password, pswd.encode('utf-8')):
            # If the credentials are valid, generate an access token for the user
            access_token = AccessToken.for_user(user)
            return Response({'access_token': str(access_token)}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


class SignupView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            # Hash the password before saving the user
            user = serializer.save()
            # After signup, generate a JWT token for the user
            access_token = AccessToken.for_user(user)
            return Response({'access_token': str(access_token)}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
