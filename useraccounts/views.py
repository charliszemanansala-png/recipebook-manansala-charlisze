from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin


class CustomView(LoginRequiredMixin, DetailView):
    template_name = ""
    redirect_field_name = ""
