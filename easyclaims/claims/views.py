from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from claims.models import List
from claims.serializers import ListForm
from django.http import JsonResponse
from rest_framework.decorators import api_view

class ClaimViewList(APIView):
    def get(self, request, format=None):
        snippets = List.objects.all()
        serializer =ListForm(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ListForm(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ClaimViewDetail(APIView):
     def get_object(self, pk):
        try:
            return List.objects.get(pk=pk)
        except List.DoesNotExist:
            raise Http404
     def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = ListForm(snippet)
        return Response(serializer.data)
     def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer =ListForm(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
     def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class ClaimStatusDetail(APIView):
    def get_object(self, pk):
        try:
            return List.objects.get(pk=pk)
        except List.DoesNotExist:
            raise Http404
    def post(self, request, format=None):
        serializer = ListForm(data=request.data)
        claimNo = request.data['queryResult']['parameters']['number'] 
        snippet = self.get_object(claimNo)
        serializer = ListForm(snippet)
        claim_status = serializer.data['status']
        return Response({"fullfillmenttext":claim_status},safe=False)

class DialogFLowClaimHelper(APIView):
    def post(self, request, format=None):
        #fetch dialogueflow json
        claimNo = request.data['queryResult']['parameters']['number'] 
        claim = ListForm(List.objects.get(pk=claimNo))
        return Response(claim.data, status=status.HTTP_200_OK)
