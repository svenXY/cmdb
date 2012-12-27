# Create your views here.

from django.shortcuts import render_to_response, get_object_or_404, render
from django.template import RequestContext
from django.http import HttpResponseRedirect
from cmdb.models import CiHardware, CiHardwareForm
from django_tables2   import RequestConfig
from cmdb.tables  import CiTable, HwPrdTable
from copy import deepcopy


#def index(request):
#        cihw = CiHardware.objects.all()
#        return render_to_response('cmdb/index.html', {'ci_list': cihw})

def index(request):
    table = CiTable(CiHardware.objects.all())
    RequestConfig(request, paginate={"per_page":25}).configure(table)
    return render(request, 'cmdb/index.html', {'table': table})

def prod_index(request):
    table = HwPrdTable(CiHardware.objects.filter(is_template=True))
    RequestConfig(request, paginate={"per_page":25}).configure(table)
    return render(request, 'cmdb/index.html', {'table': table})


def detail(request, ci_id):
    ci = get_object_or_404(CiHardware, pk=ci_id)
    return render_to_response('cmdb/detail.html', {'object' : ci})

def edit_ci(request, ci_id=None):
    if request.POST:
        if ci_id:
            ci_data = get_object_or_404(CiHardware, pk=ci_id)
            form = CiHardwareForm(instance=ci_data, data=request.POST)
        else:
            form = CiHardwareForm(data=request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/cmdb/ci/%s/' % ci_id)
    else:
        if ci_id:
            ci_data = get_object_or_404(CiHardware, pk=ci_id)
            form =  CiHardwareForm(instance=ci_data)
        else:
            form =  CiHardwareForm()

    return render_to_response('cmdb/new_hw_ci.html', {'form':form}, context_instance=RequestContext(request)) 


def new_ci(request, ci_id=None):
    if request.POST:
        if ci_id:
            ci_data = get_object_or_404(CiHardware, pk=ci_id)
            form = CiHardwareForm(instance=ci_data, data=request.POST)
        else:
            form = CiHardwareForm(data=request.POST)
        if form.is_valid():
            ci_clone = form.save(commit=False)
            ci_clone.id = None
            ci_clone.save()
        return HttpResponseRedirect('/cmdb/ci/%s/' % ci_id)
    else:
        if ci_id:
            ci_orig = get_object_or_404(CiHardware, pk=ci_id)
            ci_data = deepcopy(ci_orig)
            ci_data.name = ''
            ci_data.model = ci_orig
            ci_data.status = ''
            ci_data.comment = ''
            ci_data.usage = ''
            ci_data.is_template = False
            ci_data.create_date = None
            form =  CiHardwareForm(instance=ci_data)
        else:
            form =  CiHardwareForm()

    return render_to_response('cmdb/new_hw_ci.html', {'form':form}, context_instance=RequestContext(request)) 


