from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from library import models as lib_models
from library import serializers


@api_view(['GET', 'POST'])
def member_list(request):
    if request.method == 'GET':
        members = lib_models.Member.objects.all()
        serializer = serializers.MemberSerializer(members, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = serializers.MemberSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
