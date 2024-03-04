from rest_framework import generics
from .models import User
from .serializers import UserSerializer
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import AccessToken
from .models import User
from .serializers import UserSerializer


class UserListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class LoginView(APIView):
    def post(self, request):
        # Votre logique pour valider les informations de connexion de l'utilisateur
        user = User.objects.filter(email=request.data.get('email')).first()
        if user is not None and user.check_password(request.data.get('password')):
            # Si les informations sont valides, générer un token JWT
            access_token = AccessToken.for_user(user)
            return Response({'access_token': str(access_token)}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

class SignupView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            # Après l'inscription, générer un token JWT pour l'utilisateur
            access_token = AccessToken.for_user(user)
            return Response({'access_token': str(access_token)}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
