from django.template import Template, Context
from django.http import HttpResponse

import datetime

def saludar(request):
    return HttpResponse("Bienvenidos a la comisión 50215 - Clase Django")

def bienvenida(request, nombre, apellido):
    respuesta = f"Te damos la bienvenida a la comisión 50215 {apellido}, {nombre}"
    return HttpResponse(respuesta)

def bienvenido_html(request, nombre, apellido):
    hoy = datetime.datetime.now()
    respuesta = f"""
    <html>
    <h1>Bienvenidos al curso de Django!!</h1>
    <h2>Esta es la comisión 50215<h2>
    <h2>Te damos la bienvenida a la comisión 50215 {apellido}, {nombre}</h2>
    <h3> Hoy es {hoy} </h3>
    </html>
    """
    return HttpResponse(respuesta)

def bienvenido_template(request):
    miHtml = open("C:/Users/nicolas/Documents/Coderhouse/Clase_17/proyecto/proyecto/plantillas/bienvenido.html")
    plantilla = Template(miHtml.read())
    miHtml.close()
    contexto = Context()
    respuesta = plantilla.render(contexto)
    return HttpResponse(respuesta)