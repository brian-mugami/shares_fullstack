import traceback
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .utils import get_tokens_for_user
from .serializers import RegistrationSerializer, PasswordChangeSerializer
from . import models

from . import serializers
User = get_user_model()


class CountryView(viewsets.ViewSet):
    permission_classes = [IsAuthenticated, ]
    def create(self, request):
        country = serializers.CountrySerializer(data=request.data)
        country.is_valid(raise_exception=True)
        country.save()
        return Response(country.data)

    def destroy(self,request, pk=None):
        country = get_object_or_404(models.CountryModel, id=pk)
        country.delete()
        return Response({"msg":"deleted"})

class RegistrationView(APIView):
    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DeleteUserView(APIView):
    def delete(self, request, pk:None):
        user = get_object_or_404(models.User, id=pk)
        user.delete()
        return Response({"msg": "deleted"})

class LoginView(APIView):
    def post(self, request):
        if 'email' not in request.data or 'password' not in request.data:
            return Response({'msg': 'Credentials missing'}, status=status.HTTP_400_BAD_REQUEST)
        email = request.data['email']
        password = request.data['password']
        user = authenticate(request, email=email, password=password)
        if user:
            login(request, user)
            auth_data = get_tokens_for_user(request.user)
            return Response({'msg': 'Login Success', **auth_data}, status=status.HTTP_200_OK)
        return Response({'msg': 'Invalid Credentials'}, status=status.HTTP_401_UNAUTHORIZED)


class LogoutView(APIView):
    permission_classes = [IsAuthenticated, ]
    def post(self, request):
        logout(request)
        return Response({'msg': 'Successfully Logged out'}, status=status.HTTP_200_OK)


class ChangePasswordView(APIView):
    permission_classes = [IsAuthenticated, ]

    def post(self, request):
        serializer = PasswordChangeSerializer(context={'request': request}, data=request.data)
        serializer.is_valid(raise_exception=True)  # Another way to write is as in Line 17
        request.user.set_password(serializer.validated_data['new_password'])
        request.user.save()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ConfirmationView(APIView):
    @classmethod
    def get(cls, request, confirmation_id:str):
        confirmation = models.ConfirmationModel.find_by_id(confirmation_id)
        if not confirmation:
            return Response({"msg": "No confirmation found"}, status=status.HTTP_400_BAD_REQUEST)
        if confirmation.expired:
            return Response({"msg": "Confirmation has expired"}, status=status.HTTP_400_BAD_REQUEST)
        if confirmation.confirmed:
            return Response({"msg": "You are already confirmed"}, status=status.HTTP_400_BAD_REQUEST)
        confirmation.confirmed = True
        confirmation.save()
        user = models.ConfirmationModel.objects.select_related("user").get(id=confirmation_id)
        user_email = user.user.email
        return render(request, "confirmemail.html", {"email": user_email})

class ConfirmationByUser(APIView):
    @classmethod
    def post(cls, user_id:int):
        user = models.User.objects.get(id=user_id)
        if not user:
            return Response({"msg": "User not found"}), 404
        try:
            confirmation = user.most_recent_confirmation
            if confirmation:
                if confirmation.confirmed:
                    return Response({"msg": "Already confirmed"}), 400
                confirmation.force_to_expire()

            new_confirmation = models.ConfirmationModel(user_id)
            new_confirmation.save()
            return Response({"msg": "Resend successfull"}), 201
        except:
            traceback.print_exc()
            return Response({"msg": "Resend failed"}), 500



