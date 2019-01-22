from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import List
from .serializers import ListForm

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
     def get_status(self,request,claimnumber):
        snippets = List.objects.all()
        snippets = snippets .filter(claimNo=claimnumber)
        serializer =ListForm(snippets, many=True)
        return Response(serializer.data.status)
         

