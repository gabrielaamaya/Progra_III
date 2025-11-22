from django.http import HttpResponse
from django.utils import timezone
from django.template import Context, Template


def hora_y_fecha(request):
    now = timezone.now()

    fecha = now.strftime('%Y-%m-%d')
    hora = now.strftime('%H:%M:%S.%f')[:-3]   # milisegundos

    html_content = f"""
    <html>
    <body>
        <h3>La fecha es: {fecha}</h3d>
        <h2>La hora es: {hora}</h2>
    </body>
    </html>
    """

    return HttpResponse(html_content)



def categoriaEdad(request, edad):
    if edad >= 18:
        if edad >= 60:
            categoria = "Tercera edad"
        else:
            categoria = "adultez"
    else:
        if edad < 10:
            categoria = "Infancia"
        else:
            categoria = "Adolescencia"

    resultado = """<h1>Categoria de la edad: %s</h1>""" % categoria
    return HttpResponse(resultado)

