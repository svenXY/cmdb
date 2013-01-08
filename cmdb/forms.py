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

from django.forms import ModelForm
from models import CiHardware

class CiHardwareForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(CiHardwareForm, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance and instance.id:
            self.fields['model'].widget.attrs['disabled'] = 'disabled'
            self.fields['type'].widget.attrs['disabled'] = 'disabled'
            self.fields['is_template'].widget.attrs['disabled'] = 'disabled'

    class Meta:
        model = CiHardware

