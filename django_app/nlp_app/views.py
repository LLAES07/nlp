from django.shortcuts import render, redirect
from .models import FormSending
from .forms import FormSendingForm

# Create your views here.

def index(request):
    if request.method == 'POST':
        # Se recibe el formulario enviado
        form = FormSendingForm(request.POST)
        if form.is_valid():
            form.save()  # Guarda el nuevo registro en la base de datos
            return redirect('index')  # Redirige a la misma vista u otra, según prefieras
    else:
        # Método GET: se muestra el formulario vacío
        form = FormSendingForm()

    # Si lo deseas, también puedes obtener los datos ya ingresados para mostrarlos en la página.
    form_sendings = FormSending.objects.all()
    context = {
        'form': form,
        'form_sendings': form_sendings,
    }
    return render(request, 'index.html', context)