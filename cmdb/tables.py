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
from django_tables2.utils import A
from cmdb.models import CiHardware

class CiTable(tables.Table):
    name = tables.LinkColumn('hw_ci_edit', args=[A('pk'), 'edit'])
    aktion = tables.TemplateColumn('<a href="ci/{{record.id}}/del" title="remove CI" onClick="return confirm(\'Wirklich löschen?\');">d</a>')
    class Meta:
        model = CiHardware
        attrs = {"class": "paleblue"}
        sequence = ("name", "usage", "status", "model", "type", "comment", 
                    "...", "comment", "create_date")
        exclude = ('id', )

class HwPrdTable(CiTable):
    aktion = tables.TemplateColumn('<a href="ci/{{record.id}}/clone" title="create CI">c</a>')
    class Meta:
        attrs = {"class": "paleblue"}
        sequence = ("name", "type", "supplier", "status", "...", "create_date")
        exclude = ( 'id', "usage", "comment", "model" )

