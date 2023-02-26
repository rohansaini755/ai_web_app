from django.shortcuts import render
from rest_framework.decorators import api_view 
from .models import Text
from rest_framework.response import Response
import json
from .serializer import textSerializer
from rest_framework import status


@api_view(['POST'])
def add_text(request):
    serializer = textSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response({"message":"done"},status=status.HTTP_200_OK)

@api_view(['POST'])
def get_text_v1(request):
    pass

@api_view(['GET'])
def get_text(request):
    text1 = Text.objects.first()
    data = {}
    data['name'] = text1.name
    edata = text1.hindiText
    hex_representation = edata.encode("utf-8").hex()
    edata = hex_representation
    data['hindiText'] = edata
    data['englishText'] = text1.englishText
    hdata = text1.hintString
    hdata = hdata.encode("utf-8").hex()
    data['hintString']  = hdata
    res = Response(json.dumps(data))
    res.headers["Access-Control-Allow-Origin"] = "*"
    return res
