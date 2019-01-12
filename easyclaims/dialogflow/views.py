from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from django.core import serializers
from django.conf import settings
import json
import requests

# Create your views here.
@api_view(['POST'])
def IdealWeight():
    questionFromBot=json.loads(requests.body.decode("utf-8"))
    res = makeResponse(questionFromBot)
    res = json.dumps(res, indent=4)
    return JsonResponse(res,content_type='application/json')

def makeResponse(req):
    result = req.get('result')
    parameters = result.get('parameters')
    claimid = parameters.get('claimid')
    claimstatus="approved"
    speech = "claim status for your"+claimid+"is"+claimstatus
    return { "speech":speech,
             "displayText":speech,
             "source":"claims-api"
             }
















