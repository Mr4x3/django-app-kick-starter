# Python Imports

# Django Imports
from django.urls import path

# Third Party Django Imports
from rest_framework.urlpatterns import format_suffix_patterns

# Inter App Imports

# Local Imports
from .views import {{app_name | title}}APIView


urlpatterns = [
    path('create-{{app_name}}/', {{app_name | title}}APIView.as_view(), name='create_{{app_name}}'),  # For {{app_name | title}} App
]

# Add Multiple Format Support
urlpatterns = format_suffix_patterns(urlpatterns)
