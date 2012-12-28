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
    name = tables.TemplateColumn('<a href="ci/{{record.id }}/edit">{{record.name}}</a>')
    aktion = tables.TemplateColumn('<a href="ci/{{record.id}}/del" title="remove CI" onClick="return confirm(\'Wirklich löschen?\');">d</a>')
    class Meta:
        model = CiHardware
        attrs = {"class": "paleblue"}
        sequence = ("name", "model", "type", "usage", "comment", "status",
                    "...", "comment", "create_date")
        exclude = ('id', 'is_template' )

class HwPrdTable(CiTable):
    aktion = tables.TemplateColumn('<a href="ci/{{record.id}}/clone" title="create CI">c</a>')
    class Meta:
        attrs = {"class": "paleblue"}
        sequence = ("name", "type", "supplier", "status", "...", "create_date")
        exclude = ( 'id', "is_template",  "usage", "comment", "model" )

