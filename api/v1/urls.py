# Python Imports

# Django Imports
from django.conf.urls import url

# Third Party Django Imports
from rest_framework.urlpatterns import format_suffix_patterns

# Inter App Imports

# Local Imports
from .views import {{app_name | title}}APIView


urlpatterns = [
    url(r'^(?P<pk>\d+)/$', {{app_name | title}}APIView.as_view(), name='{{app_name}}_view'),  # For {{app_name | title}} App
]

# Add Multiple Format Support
urlpatterns = format_suffix_patterns(urlpatterns)
