from django.shortcuts import render
from django.views.generic import TemplateView
from django.db.models import Sum
from django.utils import timezone
from calendar import monthrange
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import forms as auth_forms
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.views.generic import TemplateView, RedirectView, UpdateView
from django.views.generic import FormView
from django.http import HttpResponseRedirect,HttpResponse
from .forms import RegisterForm

# class IndexView(FormView):
#     template_name = 'index.html'

#     def get_context_data(self, **kwargs):
#         context = super(IndexView, self).get_context_data(**kwargs)
#         return context


class IndexView(FormView):
    form_class = RegisterForm
    template_name = 'index.html'
    
    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect(reverse('index'))

    def form_invalid(self, form):
        return super(RegisterFormView, self).form_invalid(form)






class RegisterFormView(FormView):
    form_class = RegisterForm
    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect(reverse('index'))

    def form_invalid(self, form):
        return super(RegisterFormView, self).form_invalid(form)