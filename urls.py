# Python Imports

# Django Imports
from django.conf.urls import url, include

# Third Party Django Imports

# Inter App Imports

# Local Imports
from .views import Add{{app_name | title}}View, Detail{{app_name | title}}View, List{{app_name | title}}View, Update{{app_name | title}}View

app_name = '{{app_name}}'

# {{app_name | title}} Views Urls
urlpatterns = [
    # Apis For {{app_name | title}} App
    url(r'^api/', include('{{app_name}}.api.urls')),  # {{app_name | title}} Apis

    # {{app_name | title}} Urls
    url(r'^add/$', Add{{app_name | title}}View.as_view(), name='{{app_name}}_add'),  # Add {{app_name | title}}
    url(r'^(?P<pk>\d+)/detail/$', Detail{{app_name | title}}View.as_view(), name='{{app_name}}_detail'),  # Detail {{app_name | title}}
    url(r'^list/$', List{{app_name | title}}View.as_view(), name='{{app_name}}_list'),  # List {{app_name | title}}
    url(r'^(?P<slug>[-\w]+)/update/$', Update{{app_name | title}}View.as_view(), name='{{app_name}}_update'),  # Update {{app_name | title}}
    url(r'^{{app_name}}/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/(?P<day>[0-9]{2})/$', Update{{app_name | title}}View.as_view(), name='{{app_name}}_years'),  # Years {{app_name | title}}
]
