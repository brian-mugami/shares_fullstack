from rest_framework import serializers
from django.contrib.auth import get_user_model

from . import models

User = get_user_model()

class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={"input_type": "password"}, write_only=True)
    class Meta:
        model = User
        fields = ['id', 'email', 'date_of_birth', 'password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def save(self):
        user = User(email=self.validated_data['email'], date_of_birth=self.validated_data['date_of_birth'])
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        if password != password2:
            raise serializers.ValidationError({'password': 'Passwords must match.'})
        user.set_password(password)
        user.save()

class LoginSerializer(serializers.Serializer):
    class Meta:
        model = User
        fields = ["email", "password"]

        def validate_user(self, value):
            if not self.context['request'].user.check_password(value):
                raise serializers.ValidationError({"msg": "Password is wrong" })
            return value

class PasswordChangeSerializer(serializers.Serializer):
    current_password = serializers.CharField(style={"input_type": "password"}, required=True)
    new_password = serializers.CharField(style={"input_type": "password"}, required=True)

    def validate_current_password(self, value):
        if not self.context['request'].user.check_password(value):
            raise serializers.ValidationError({'current_password': 'Does not match'})
        return value

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CountryModel
        fields = "__all__"

class ConfirmationSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=models.User.objects.all())
    class Meta:
        model = models.ConfirmationModel
        fields = "__all__"
        read_only_fields = ["id", "expire_at", "confirmed"]


