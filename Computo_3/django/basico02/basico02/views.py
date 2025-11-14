from django.http import HttpResponse
from django.utils import timezone

def hora_y_fecha(request):
    now = timezone.now()

    fecha = now.strftime('%Y-%m-%d')
    hora = now.strftime('%H:%M:%S.%f')[:-3]   # milisegundos

    html_content = f"""
    <html>
    <body>
        <h3>La fecha es: {fecha}</h3>
        <h2>La hora es: {hora}</h2>
    </body>
    </html>
    """

    return HttpResponse(html_content)