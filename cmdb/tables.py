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

import django_tables2 as tables
from cmdb.models import CiHardware

class CiTable(tables.Table):
    name = tables.TemplateColumn('<a href="ci/{{record.id}}/">{{record.name}}</a>')
    links = tables.TemplateColumn('''
            <a href="/cmdb/ci/{{record.id}}/clone" title="clone as new">c</a> |
            <a href="ci/{{record.id}}/edit" title="edit">e</a>''')
    class Meta:
        model = CiHardware
        attrs = {"class": "paleblue"}
        sequence = ("id", "name", "model", "status", "usage", "comment", "type", "...", "create_date", "links")

class HwPrdTable(CiTable):
    class Meta:
        attrs = {"class": "paleblue"}
        sequence = ("id", "name", "type", "supplier", "status", "...", "create_date")
        exclude = ( "is_template",  "usage", "comment", "model" )

