from django.http import HttpResponse
from datetime import datetime
from django.http import JsonResponse


def ping(request):
        data = {
            "new" : datetime.now()
        }
        return JsonResponse(data)