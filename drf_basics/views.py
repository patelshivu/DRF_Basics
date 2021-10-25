from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from rest_framework import status
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view, authentication_classes, permission_classes

# Create your views here.
@api_view(["GET"])
def test_deploy(request):
    response = {
                "message": "Testing DRF application",
                "status": 200
            }
    return JsonResponse(response,status=200)
