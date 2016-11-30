# Python Imports

# Django Imports

# Third Party Django Imports
from rest_framework import serializers

# Inter App Imports

# Local Imports


class {{ app_name|title }}Serializer(serializers.ModelSerializer):
    """
    Serializer For Serialization Of {{ app_name|title }} Fields
    """
    # class Meta:
    #     model = {{ app_name|title }}
    #     fields = []
