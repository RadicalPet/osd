from __future__ import unicode_literals
from django.shortcuts import render

from django.views.generic.base import TemplateView
from django.contrib import messages
from django.core.files.storage import default_storage

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models.fields.files import FieldFile
from django.views.generic import FormView

class IndexView(TemplateView):
    template_name = 'osd/index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        messages.info(self.request, 'welcome to osd')
        return context
