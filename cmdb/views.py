# Create your views here.

from django.http import HttpResponse, Http404
from django.template import Context, loader
from cmdb.models import CiHardware


def index(request):
        cihw = CiHardware.objects.all()
        t = loader.get_template('cmdb/index.html')
        c = Context({'object_list': cihw})
        return HttpResponse(t.render(c))


def detail(request, ci_id):
    try:
        ci = CiHardware.objects.get(id=ci_id)
    except CiHardware.DoesNotExist:
        raise Http404
    t = loader.get_template('cmdb/detail.html')
    c = Context({'object' : ci})
    return HttpResponse(t.render(c))
