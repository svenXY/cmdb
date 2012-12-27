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
from django.conf.urls import patterns, url

urlpatterns = patterns('cmdb.views',
        url(r'^ci/(?P<ci_id>\d+)/$', 'detail'),
        url(r'^ci/(?P<ci_id>\d+)/edit$', 'edit_ci'),
        url(r'^prd', 'prod_index'),
        url(r'$', 'index'),
)
