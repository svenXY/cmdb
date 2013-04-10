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
        url(r'^ci/(?P<ci_id>\d+)$', 'hw_ci_detail'),
        url(r'^ci/(?P<ci_id>\d+)/(?P<action>edit)$', 'hw_ci_mgt',
            name='hw_ci_edit'),
        url(r'^ci/(?P<ci_id>\d+)/(?P<action>clone)$', 'hw_ci_mgt'),
        url(r'^ci/(?P<ci_id>\d+)/(?P<action>del)$', 'hw_ci_mgt'),
        url(r'^prd$', 'hw_prd_index'),
        url(r'^ci$', 'hw_ci_index'),
                       #url(r'$', 'hw_ci_index'),
)
