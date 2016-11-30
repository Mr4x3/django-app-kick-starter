# Python Imports
import unittest
import os
import shutil
import base64
from datetime import datetime, timedelta

# Django Imports
from django.contrib.auth.models import AnonymousUser
from django.test import Client, TestCase, RequestFactory
from django.forms.models import model_to_dict
from django.core.urlresolvers import reverse, reverse_lazy
from django.conf import settings
from django.contrib.auth.models import User

# Third Party Django Imports
import pytest
from mixer.backend.django import mixer

# Inter App Imports
from customer import views, models, forms
from customer.models import Customer, Complain
from company.models import Company, StaffMember

# Local Imports


pytestmark = pytest.mark.django_db  # Used As py.test Give Error When Saved To Database


# Tests For {{ app_name|title }}
