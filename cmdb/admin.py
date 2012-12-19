#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Name			:	
# Description	:	
# Author		: Sven Hergenhahn
#
# $Id$
# 
###################################################

from django.contrib import admin
from .models import CiHardware, Category

admin.site.register(CiHardware)
admin.site.register(Category)


