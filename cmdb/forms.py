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

from django.forms import ModelForm, HiddenInput
from models import CiHardware

class CiHardwareForm(ModelForm):
    class Meta:
        model = CiHardware
        exclude = { 'date_created', }
        widgets = { 
            'name' : HiddenInput,
            'model' : HiddenInput
        }

