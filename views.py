# Python Imports
from datetime import datetime

# Django Imports
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import FormView, ListView, DetailView, TemplateView
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, render_to_response, get_object_or_404
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.db.models import F

# Third Party Django Imports
# from openpyxl import load_workbook
# from openpyxl.writer.excel import save_virtual_workbook
# from openpyxl import Workbook
# from pytz import timezone as tz

# Inter App Imports

# Local Imports


# Views For {{app_name | title}}
