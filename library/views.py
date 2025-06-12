from django.shortcuts import render
from django.http import Http404
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, APIView
from library import models as lib_models
from library import serializers


class MemberList(APIView):
    """
    List all members or createa new one.
    """
    def get(self, request, format=None):
        members = lib_models.Member.objects.all()
        serializer = serializers.MemberSerializer(members, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = serializers.MemberSerializer(data=request.data)
        print(f"\n\n\ntype: {type(request.data)}, d: {(request.data)}")
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST0)
    

class MemberDetail(APIView):
    """
    Retrive, update or delete a member.
    """
    def get_object(self, pk):
        try:
            return lib_models.Member.objects.get(pk=pk)
        except lib_models.Member.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        member = self.get_object(pk=pk)
        serializer = serializers.MemberSerializer(member)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        member = self.get_object(pk=pk)
        serializer = serializers.MemberSerializer(member, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        member = self.get_object(pk=pk)
        member.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    