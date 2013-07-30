import json
import random
from django.http import HttpResponse
import psutil


def stats(request):
    some_data = {
        'cpu':  psutil.cpu_percent(),
        'mem':  psutil.virtual_memory().percent,
        'swap': psutil.swap_memory().percent,
        'disk': psutil.disk_usage('/').percent
    }
    data = json.dumps(some_data)
    return HttpResponse(data, mimetype='application/json')
