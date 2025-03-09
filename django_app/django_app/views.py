import os
import pickle
from django.conf import settings
from django.shortcuts import render
from django.http import JsonResponse
from pathlib import Path
from django_app.utils import predict_label




def main_view(request):
    # Renderiza la plantilla principal con el input
    return render(request, 'main.html')

def predict_api(request):
    """
    Endpoint para predecir con el modelo.
    Retorna un JSON con la predicción.
    """
    if request.method == 'POST':
        # Obtener el texto enviado desde JavaScript
        user_text = request.POST.get('text', '')
    
        prediction = predict_label(user_text)

        # Retorna un JSON con el resultado
        return JsonResponse({'prediction': prediction})
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)
