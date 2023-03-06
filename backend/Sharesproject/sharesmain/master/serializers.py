from rest_framework import serializers
from django.contrib.auth import get_user_model

from . import models
User = get_user_model()
class SharesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SharesMaster
        fields = "__all__"

        read_only_fields = ["id", "is_archived", "date_created", "last_updated"]

class SharesUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SharesMaster
        fields = []

class UserShareSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    share = serializers.PrimaryKeyRelatedField(queryset=models.SharesMaster.objects.all())
    class Meta:
        model = models.UserSharesMaster
        fields = "__all__"

class UserShareWatchlistSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    share = serializers.PrimaryKeyRelatedField(queryset=models.SharesMaster.objects.all())

    class Meta:
        model = models.UserShareWatchlist
        read_only_fields = ["id", "watched_price"]
