from dataclasses import field
from gettext import gettext
from django import forms
from .models import Sites
import gettext
from django.contrib import messages
_ = gettext.gettext


class CheckForm(forms.Form):
    domain_form = forms.CharField()

