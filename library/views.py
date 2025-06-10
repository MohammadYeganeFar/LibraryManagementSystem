from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from library import models as lib_models
from library import serializers

@csrf_exempt
def member_list(request):
    if request.method == 'GET':
        members = lib_models.Member.objects.all()
        serializer = serializers.MemberSerializer(members, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    elif request.method == 'POST':
        print(f'request: {request}, type: {type(request)}')
        data = JSONParser().parse(request)
        serializer = serializers.MemberSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

        
