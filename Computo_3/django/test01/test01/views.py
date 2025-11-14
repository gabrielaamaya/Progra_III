from django.http import HttpResponse

def saludo(request):  # esta es mi primera vista
    pagina = """
    <html>
    <body>
    <h2>
    Hola Mundo, esta es mi primera vista en Django!
    </h2>
    </body>
    </html>"""
    return HttpResponse(pagina)


def despedida(request):  # esta es mi segunda vista
    return HttpResponse("""
        <html>
            <body style="background-color:#f0f8ff; text-align:center; padding-top:100px;">
                <h1 style="font-size:36px; color:#0077cc; font-family:Arial, sans-serif;">
                    ¡Fue un gusto trabajar con ustedes! 
                </h1>
            </body>
        </html>
    """)


def calculadora(request, agno):
    edadactual = 32
    agoactual = 2025
    tiempo = agno - agoactual
    edadfutura = edadactual + tiempo
    return HttpResponse(f"""
        <html>
            <body style="background-color:#f4f4f4; text-align:center; padding-top:100px;">
                <h1 style="font-size:30px; color:#333;">
                    En el año {agno}, tendrás {edadfutura} años
                </h1>
            </body>
        </html>
    """)


def operaciones(request, num1, num2):
    suma = num1 + num2
    resta = num1 - num2
    multiplicacion = num1 * num2
    division = round(num1 / num2, 2) if num2 != 0 else "No se puede dividir entre 0"

    return HttpResponse(f"""
        <html>
            <body style="background-color:#FFFFFF; text-align:center; padding-top:50px; font-family:Arial;">
                <h2 style="color:#2e7d32;">Operaciones Básicas</h2>
                <p><strong>Primer número:</strong> {num1}</p>
                <p><strong>Segundo número:</strong> {num2}</p>
                <hr style="width:50%;">
                <p><strong>Suma:</strong> {suma}</p>
                <p><strong>Resta:</strong> {resta}</p>
                <p><strong>Multiplicación:</strong> {multiplicacion}</p>
                <p><strong>División:</strong> {division}</p>
            </body>
        </html>
    """)

