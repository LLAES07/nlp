from django.shortcuts import render, redirect
from .models import FormSending
from .forms import FormSendingForm
from django.http import JsonResponse

def index(request):
    if request.method == 'POST':
        print("¡Llegó un POST!")  
        form = FormSendingForm(request.POST)
        if form.is_valid():
            form.save()
            print("¡Se guardó el registro!")
            return redirect('nlp_app:index') 
        else:
            print("Errores del formulario:", form.errors)
    else:
        form = FormSendingForm()

    form_sendings = FormSending.objects.all()
    context = {
        'form': form,
        'form_sendings': form_sendings,
    }
    return render(request, 'index.html', context)



def get_records(request):
    records = []
    
    for registro in FormSending.objects.all().order_by('-created_at'):
        # Obtenemos el registro de ByPass asociado; asumimos que hay solo uno.
        bypass = registro.bypass_set.first()
        status = "Aprobado" if bypass and bypass.status else "Denegado"
        records.append({
            'descripcion': registro.descripcion,
            'nombre': registro.nombre,
            'categoria': registro.category.clasificacion if registro.category else "",
            'status': status,
        })
    return JsonResponse({'records': records})