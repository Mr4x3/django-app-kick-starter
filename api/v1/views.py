# Python Imports
import hashlib
import datetime

# Django Imports
from django.shortcuts import get_object_or_404
from django.conf import settings

# Third Party Django Imports
from rest_framework.views import APIView
from rest_framework.generics import RetrieveAPIView, GenericAPIView, CreateAPIView, UpdateAPIView, ListCreateAPIView, DestroyAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

# Inter App Imports

# Local Imports
from .serializers import {{app_name | title}}Serializer


class {{app_name | title}}APIView(APIView):
    """
    API For {{app_name | title}}

    URL: {{app_name}}/api/auth/v1/1.json
    Method Allowed: ['GET']
    Params: field_1, field_2

    Example: {
        "mobile_number": "8982914389",
        "is_active": "true",
    }
    """
    permission_classes = [IsAuthenticated, ]
    allowed_methods = ['GET']
    serializer_class = {{app_name | title}}Serializer
