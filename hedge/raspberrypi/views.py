import json
from django.http import HttpResponse
from . import system_utils


def stats(request):

    some_data = {
        'cpu':  system_utils.cpu_usage(),
        'mem':  system_utils.memory_usage(),
        'swap': system_utils.swap_usage(),
        'disk': system_utils.disk_usage(),
        'temp': system_utils.cpu_temperature()
    }

    data = json.dumps(some_data)
    return HttpResponse(data, mimetype='application/json')
