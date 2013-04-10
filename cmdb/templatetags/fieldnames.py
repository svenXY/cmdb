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

from django import template

register = template.Library()

@register.filter
def verbose_name(value, field):
    '''return the verbose name of the given field of the object'''
    return value._meta.get_field(field).verbose_name.capitalize() 

@register.filter
def value_with_field(value, field):
    '''Return the field with its verbose field name in 'field : value' format'''
    f = value._meta.get_field(field).verbose_name.capitalize() 
    v = str(getattr(value, field))
    return ' '.join([f, ':', v])
