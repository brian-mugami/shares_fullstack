from django.shortcuts import render
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from django.shortcuts import get_object_or_404

from . import serializers
from . import models

class MainShareView(ViewSet):
    permission_classes = [IsAuthenticated, ]

    def create(self, request):
        share = serializers.SharesSerializer(data=request.data)
        share.is_valid(raise_exception=True)
        share.save()
        return Response({"msg": "Created"}, status=status.HTTP_201_CREATED)

    def list(self, request):
        shares = models.SharesMaster.objects.all()
        serializer = serializers.SharesSerializer(shares, many=True)
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, pk:None):
        share = get_object_or_404(models.SharesMaster, id=pk)
        share.delete()
        return Response({"msg": "Deleted"}, status=status.HTTP_204_NO_CONTENT)

    def retrieve(self, request, pk:None):
        share = get_object_or_404(models.SharesMaster, id=pk)
        data = serializers.SharesSerializer(share)
        return Response(data.data, status=status.HTTP_202_ACCEPTED)

    def update(self, request, pk:None):
        share = get_object_or_404(models.SharesMaster, id=pk)
        if not share:
            return Response({"msg": "Share not available"}, status=status.HTTP_404_NOT_FOUND)
        serializer = serializers.SharesSerializer(instance=share, data=request.data)
        serializer.is_valid(raise_exception=True)
        share.update_share(request.data["current_price"])
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def archive(self, request, pk:None):
        share = get_object_or_404(models.SharesMaster, id=pk)
        if not share:
            return Response({"msg": "Share not available"}, status=status.HTTP_404_NOT_FOUND)
        share.archive_share()
        return Response({"msg":"archived"}, status=status.HTTP_202_ACCEPTED)

class UserMainShareView(ViewSet):

    def list(self, request):
        shares = models.UserSharesMaster.objects.all()
        serializer = serializers.UserShareSerializer(shares, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        share = serializers.UserShareSerializer(data=request.data)
        share.is_valid(raise_exception=True)
        share.save()
        return Response(share.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk:None):
        share_transacted = get_object_or_404(models.UserSharesMaster, id=pk)
        if not share_transacted:
            return Response({"msg": "Share not transacted"}, status=status.HTTP_404_NOT_FOUND)
        serializer=serializers.UserShareSerializer(instance=share_transacted, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, pk:None):
        share = get_object_or_404(models.UserSharesMaster, id=pk)
        share.delete()
        return Response({"msg": "Deleted"}, status=status.HTTP_204_NO_CONTENT)

    def retrieve(self, request, pk:None):
        share = get_object_or_404(models.UserSharesMaster, id=pk)
        serializer = serializers.UserShareSerializer(share)
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

class UserWatchlistView(ViewSet):
    def list(self, request):
        shares = models.UserShareWatchlist.objects.all()
        serializer = serializers.UserShareWatchlistSerializer(shares, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        share = serializers.UserShareWatchlistSerializer(data=request.data)
        share.is_valid(raise_exception=True)
        share.save()
        return Response(share.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk:None):
        share = get_object_or_404(models.UserShareWatchlist, id=pk)
        data = serializers.SharesSerializer(data=share)
        return Response(data.data, status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, pk:None):
        share = get_object_or_404(models.UserShareWatchlist, id=pk)
        share.delete()
        return Response({"msg": "Deleted"}, status=status.HTTP_204_NO_CONTENT)

    def update(self, request, pk:None):
        share_transacted = get_object_or_404(models.UserShareWatchlist, id=pk)
        if not share_transacted:
            return Response({"msg": "Share not transacted"}, status=status.HTTP_404_NOT_FOUND)
        serializer = serializers.UserShareSerializer(instance=share_transacted, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)