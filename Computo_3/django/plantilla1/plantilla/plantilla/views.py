

from django.http import HttpResponse
from django.template import Context, Template
 
def helloword(resquest):
    return HttpResponse("Hola mundo, desde Django")
 
def miPrimerPlantilla(request):
    plantillaExterna = open("C:/Users/AMAYA/Desktop/programcion III en visual code/Progra_III/Computo_3/django/plantilla1/plantilla/plantilla/miPlantilla.html")
    plantilla01 = Template(plantillaExterna.read())
    plantillaExterna.close()
    Contexto= Context()
    pagina01=plantilla01.render(Contexto)
    return HttpResponse(pagina01)


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


def miprimeraplantilla(request):
    nombre = "Lissette"
    plantillaExterna = open("C:/Users/AMAYA/Desktop/programcion III en visual code/Progra_III/Computo_3/django/plantilla1/plantilla/plantilla/miPlantilla.html")
    plantilla01 = Template(plantillaExterna.read())
    plantillaExterna.close()
    Contexto= Context({"nombreUser": nombre})
    pagina01=plantilla01.render(Contexto)
    return HttpResponse(pagina01)