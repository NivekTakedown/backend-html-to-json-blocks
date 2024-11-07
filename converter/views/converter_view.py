from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.
@api_view(['GET'])
def default_html_to_json_blocks(request):
    name = request.GET.get('name', 'html')
    data = {
        'name': name,
        'message': f"Hello {name}, your first API endpoint has been created successfully!"
    }
    return Response(data, status=status.HTTP_200_OK)