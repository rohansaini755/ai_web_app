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
    text1 = Text.objects.all()
    # data = {}
    text = []
    for it in text1:
        data = {}    
        data['name'] = it.name
        edata = it.hindiText
        hex_representation = edata.encode("utf-8").hex()
        edata = hex_representation
        data['hindiText'] = edata
        data['englishText'] = it.englishText
        hdata = it.hintString
        hdata = hdata.encode("utf-8").hex()
        data['hintString']  = hdata
        text.append(data)

    res = Response(json.dumps(text))
    res.headers["Access-Control-Allow-Origin"] = "*"
    return res
