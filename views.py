# Python Imports
import datetime

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

# Inter App Imports

# Local Imports
from .forms import {{app_name | title}}Form
from .models import {{app_name | title}}


# Views For {{app_name | title}}
class Add{{app_name | title}}View(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    """
    View To Add A {{app_name | title}}.
    """

    model = {{app_name | title}}
    form_class = {{app_name | title}}Form
    permission_required = (,)
    template_name = 'app_name/app_name_form.html'
    success_url = reverse_lazy('app_name:app_name_list')
    success_message = '{{app_name | title}} Added Successfully!!'


class Detail{{app_name | title}}View(LoginRequiredMixin, SuccessMessageMixin, DetailView):
    """
    View To Get Detail Of A {{app_name | title}}.
    """

    model = {{app_name | title}}
    context_object_name = '{{app_name}}'


class List{{app_name | title}}View(LoginRequiredMixin, StaffRequiredMixin, ListView):
    """
    List All {{app_name | title}}s.
    """

    model = {{app_name | title}}
    paginate_by = 10


class Update{{app_name | title}}View(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    """
    Update A {{app_name | title}}'s Data.
    """

    model = {{app_name | title}}
    success_url = reverse_lazy('app_name:app_name_list')
    success_message = '{{app_name | title}} Updated Successfully!!'
    fields = ('field',)
    form_class = {{app_name | title}}Form
