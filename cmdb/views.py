# Create your views here.

from django.shortcuts import render_to_response, get_object_or_404, render
from django.template import RequestContext
from django.http import HttpResponseRedirect
from cmdb.models import CiHardware, CiHardwareForm
from django_tables2   import RequestConfig
from cmdb.tables  import CiTable, HwPrdTable
from copy import deepcopy
import logging
from pprint import pformat

logger = logging.getLogger(__name__)

def hw_ci_index(request):
    ''' Return the table of all hardware CIs '''
    table = CiTable(CiHardware.objects.exclude(model_id=None))
    RequestConfig(request, paginate={"per_page":25}).configure(table)
    return render(request, 'cmdb/ci_hw_index.html', {'table': table})

def hw_prd_index(request):
    ''' Return the table of all hardware products '''
    table = HwPrdTable(CiHardware.objects.filter(model_id=None))
    RequestConfig(request, paginate={"per_page":25}).configure(table)
    return render(request, 'cmdb/ci_hw_index.html', {'table': table})

def hw_ci_detail(request, ci_id):
    ''' Return the details of a hardware CI '''
    ci = get_object_or_404(CiHardware, pk=ci_id)
    return render_to_response('cmdb/ci_hw_detail.html', {'object' : ci})

def new_product(request, ci_id=None):
    ''' Return a form to add a new product
    TODO: This does not currently work!
    '''
    if request.POST:
        if ci_id:
            ci_data = get_object_or_404(CiHardware, pk=ci_id)
            form = CiHardwareForm(instance=ci_data, data=request.POST)
        else:
            form = CiHardwareForm(data=request.POST)
        if form.is_valid():
            ci_clone = form.save(commit=False)
            ci_clone.model=None
            ci_clone.save()
        return HttpResponseRedirect('/cmdb/ci/%s' % ci_clone.id)
    else:
        if ci_id:
            ci_data = get_object_or_404(CiHardware, pk=ci_id)
            ci_clone.model=None
            form =  CiHardwareForm(instance=ci_data)
        else:
            form =  CiHardwareForm()
    return render_to_response('cmdb/ci_hw_form.html', {'form':form}, context_instance=RequestContext(request)) 

def hw_ci_mgt(request, ci_id=None, action=None):
    ''' Multipurpose view to delete, add or modify a CI, depending on the value of action '''
    prd_fields = [ 'model', 'type', 'vendor', 'supplier', 'dimensions' ]
    if action== 'del':
        ci = get_object_or_404(CiHardware, pk=ci_id)
        name = ci.name
        ci.delete()
        logger.info("Deleted hardware CI: %s" % name)
        return HttpResponseRedirect('/cmdb/ci')
    if request.POST:
        if ci_id:
            ci_data = get_object_or_404(CiHardware, pk=ci_id)
            POST = request.POST.copy()
            POST['type'] = ci_data.type_id
            if action == 'clone':
                POST['model'] = ci_id
            else:
                POST['model'] = ci_data.model_id
            form = CiHardwareForm(instance=ci_data, data=POST)
        else:
            logger.warn("CI ID is empty")
            form = CiHardwareForm(data=request.POST)
        if form.is_valid():
            ci_clone = form.save(commit=False)
            if action == 'clone':
                ci_clone.id = None
            ci_clone.save()
            return HttpResponseRedirect('/cmdb/ci/%s' % ci_clone.id)
        else:
            logger.warn("form validation failed: %s" % pformat(form.errors))
            return render_to_response('cmdb/ci_hw_form.html', {'action':action, 'form':form}, context_instance=RequestContext(request)) 
    else:
        ci = {}
        if ci_id:
            ci_orig = get_object_or_404(CiHardware, pk=ci_id)
            if action == 'clone':
                ci_data = deepcopy(ci_orig)
                ci_data.name = ''
                ci_data.model = ci_orig
                ci_data.status = ''
                ci_data.comment = ''
                ci_data.usage = ''
                ci['model'] = ci_orig.name
                ci['type'] = ci_orig.type
            elif action == 'edit':
                ci_data = ci_orig
                ci['model'] = ci_orig.model
                ci['type'] = ci_orig.type
            form =  CiHardwareForm(instance=ci_data)
        else:
            form =  CiHardwareForm()
    return render_to_response('cmdb/ci_hw_form.html', 
                                  {'action':action,
                                   'form':form, 
                                   'prd':ci_orig,
                                   'prd_fields':prd_fields
                                  }, 
                              context_instance=RequestContext(request)
                             ) 

