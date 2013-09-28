from django.http import HttpResponse
from .stats import Stats


def stats(request):
    data = Stats().to_json()
    return HttpResponse(data, mimetype='application/json')
