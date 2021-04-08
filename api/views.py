from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view

from .serializer import MessageSerializer
from .models import Message

@csrf_exempt
@api_view(['GET', 'POST'])
def messages_single(request, page = None):
    if request.method == 'GET':
        messages = Message.objects.order_by('id')
        if page != None:
            try:
                messages = messages[page - 1]
            except IndexError:
                messages = {}
            finally:
                message_serializer = MessageSerializer(messages, many = False)         
        else:
            message_serializer = MessageSerializer(messages, many = True)
        return JsonResponse(message_serializer.data, safe = False)
    
    elif request.method == 'POST':
        messages_data = JSONParser().parse(request)
        message_serializer = MessageSerializer(data = messages_data)
        if message_serializer.is_valid():
            message_serializer.save()
            return JsonResponse(message_serializer.data, status = status.HTTP_201_CREATED)
        return JsonResponse(message_serializer.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def messages_list(request, page):
    if request.method == 'GET':
        if page is not None:
            per_page = 10
            messages = Message.objects.order_by('id')[(page - 1) * per_page: (page - 1) * per_page + per_page]
        
        message_serializer = MessageSerializer(messages, many = True)
        return JsonResponse(message_serializer.data, safe = False)