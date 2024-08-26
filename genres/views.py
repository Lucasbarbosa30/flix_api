import json
from rest_framework import generics
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from genres.models import Genre
from django.shortcuts import get_object_or_404
from genres.serializers import GenreSerializer
from rest_framework.permissions import IsAuthenticated
from genres.permissions import GenrePermissionClass
from app.permissions import GlobalDefaultPermission


class GenreCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset  = Genre.objects.all() #qual banco de dados
    serializer_class = GenreSerializer

class GenreRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

