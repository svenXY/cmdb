# Create your views here.

from django.shortcuts import render_to_response, get_object_or_404
from cmdb.models import CiHardware


def index(request):
        cihw = CiHardware.objects.all()
        return render_to_response('cmdb/index.html', {'object_list': cihw})

def prod_index(request):
        cihw = CiHardware.objects.filter(is_template=True)
        return render_to_response('cmdb/index.html', {'object_list': cihw})


def detail(request, ci_id):
    ci = get_object_or_404(CiHardware, pk=ci_id)
    return render_to_response('cmdb/detail.html', {'object' : ci})
