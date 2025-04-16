
# def agendar_cita(request):
#     if request.method == 'POST':
#         form = CitaForm(request.POST)
#         if form.is_valid():
#             cita = form.save()

#             try:
#                 # Enviar correo
#                 send_mail(
#                     subject='Confirmación de cita',
#                     message=f'Hola {cita.nombre}, tu cita ha sido agendada para el {cita.fecha} a las {cita.hora}.',
#                     from_email=settings.DEFAULT_FROM_EMAIL,
#                     recipient_list=[cita.correo],
#                     fail_silently=False,
#                 )
#             except BadHeaderError:
#                 return HttpResponse('Encabezado inválido.')

#             return redirect('confirmacion')  # Redirecciona a una vista de confirmación
#     else:
#         form = CitaForm()

#     return render(request, 'agendador/formulario.html', {'form': form})


# def agendar_cita(request):
#     if request.method == 'POST':
#         form = CitaForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return render(request, 'agendador/confirmacion.html')
#     else:
#         form = CitaForm()
#     return render(request, 'agendador/formulario.html', {'form': form})
from django.shortcuts import render, redirect
from .forms import CitaForm
from django.core.mail import send_mail, BadHeaderError
from django.conf import settings
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Cita
from datetime import datetime
from django.contrib.auth.decorators import login_required
import logging
logger = logging.getLogger(__name__)

def agendar_cita(request):
    return render(request, 'agendador/formulario.html')

@csrf_exempt
def webhook_cal(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            p@csrf_exempt
def webhook_cal(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            payload = data.get('payload', {})

            nombre = payload.get('name', 'Sin nombre')
            correo = payload.get('email', '')
            start_time = payload.get('start_time', '')  # ← Cal.com usa snake_case por default

            logger.warning("Webhook recibido:\n%s", json.dumps(payload, indent=2))

            if start_time:
                fecha_obj = datetime.fromisoformat(start_time.replace('Z', '+00:00'))
                fecha = fecha_obj.date()
                hora = fecha_obj.time()

                Cita.objects.create(
                    nombre=nombre,
                    correo=correo,
                    telefono='-',  # Cal no manda esto por default
                    fecha=fecha,
                    hora=hora,
                    confirmado=True
                )
                logger.info("✅ Cita creada correctamente para %s", nombre)
                return JsonResponse({'status': 'ok'}, status=200)

            return JsonResponse({'error': 'start_time inválido'}, status=400)

        except Exception as e:
            logger.error("❌ Error en webhook: %s", str(e))
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': 'Método no permitido'}, status=405)


@login_required
def dashboard_citas(request):
    citas = Cita.objects.order_by('-creado_en')
    return render(request, 'agendador/dashboard.html', {'citas': citas})
