# Python Imports
import os
import uuid

# Django Imports
from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import User

# Third Party Django Imports

# Inter App Imports

# Local Imports


# Models For {{app_name | title}}
def get_{{app_name}}_photo_upload_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = '{0}.{1}'.format(uuid.uuid4(), ext)
    return os.path.join('{{app_name}}', filename)


class {{app_name | title}}(models.Model):
    """
    Model For {{app_name | title}}.
    """
    name = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to=get_{{app_name}}_photo_upload_path, blank=True, null=True)
    attached_persons = models.ManyToManyField({{app_name | title}}, related_name='models')
    mobile = models.CharField(max_length=10, blank=True, null=True, validators=[validate_contact_number])
    company_type = models.CharField(max_length=4, choices=COMPANY_TYPE, blank=True, null=True)
    p_contact_person = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.name
