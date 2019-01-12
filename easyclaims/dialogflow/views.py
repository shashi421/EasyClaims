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
def IdealWeight(arg):
    try:
        questionToBot=json.loads(arg.body)

        response = requests.get(
            'https://api.dialogflow.com/v1/query?v=20150910&lang=en&query='+questionToBot+'&sessionId=12345',
            headers={
                'Authorization': 'Bearer 9f00279a2f2a4be6b7bf30b3ccb46390'
            }
        )

        # extracting data in json format
        data = response.json()
        ansFromBot = data['result']['fulfillment']['speech']

        return JsonResponse(ansFromBot,safe=False)
    except ValueError as e:
        return Response(e.args[0],status.HTTP_400_BAD_REQUEST)
