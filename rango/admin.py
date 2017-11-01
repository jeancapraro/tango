# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Category, Page

# Register your models here.
admin.site.register(Category)
admin.site.register(Page)