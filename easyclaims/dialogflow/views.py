from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from django.core import serializers
from django.conf import settings
from rest_framework.decorators import parser_classes
from rest_framework.parsers import JSONParser
import json
import requests
import io

# Create your views here.
@api_view(['POST'])
def IdealWeight(request):
    try:
        #stream = io.BytesIO(json)
        questionToBot = JSONParser().parse(request)
        #questionToBot=json.loads("request data")
        question = questionToBot["question"]
        response = requests.get(
            'https://api.dialogflow.com/v1/query?v=20150910&lang=en&query='+question+'&sessionId=12345',
            headers={
                'Authorization': 'Bearer aaa4b2120df34b37aea56f6e9d97a5ef'
            }
        )

        # extracting data in json format
        data = response.json()
        ansFromBot = data['result']['fulfillment']['speech']

        return JsonResponse(ansFromBot,safe=False)
    except ValueError as e:
        return Response(e.args[0],status.HTTP_400_BAD_REQUEST)
