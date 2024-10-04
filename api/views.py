from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from googletrans import Translator  # Install googletrans for translation

@api_view(['POST'])
def translate_user_info(request):
    data = request.data.get('info', [])
    if not data:
        return Response({"error": "No data provided"}, status=400)

    translator = Translator()
    translated_info = [translator.translate(text, dest='de').text for text in data]

    return Response({"translated_info": translated_info})
