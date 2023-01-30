from django.http import HttpResponse
from datetime import datetime
# from django.http import JsonResponse


def ping(request):
        data = {
            "message" : datetime.now()
        }
        return HttpResponse(data)