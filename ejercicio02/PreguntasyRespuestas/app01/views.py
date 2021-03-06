from django.shortcuts import render, get_object_or_404, render_to_response
from django.http import HttpResponse, Http404
from app01.models import Pregunta, Respuesta


# Create your views here.
def index(request):
    preguntas = Pregunta.objects.all()
    return render_to_response("preguntas.html",{"preguntas":preguntas})


#def pregunta_detalle(self, pregunta_id):
#    pregunta = Pregunta.objects.get(pk=pregunta_id)
#    return HttpResponse("%s" % pregunta.asunto)


#Lo siguiente es codigo para manejar el error 404, para que en caso de que elijan un numero de pregunta que no exista este lo pueda manejar


#def pregunta_detalle(request, pregunta_id):
#    try:
#        pregunta = Pregunta.objects.get(pk=pregunta_id)
#    except Pregunta.DoesNotExist: #Si la pregunta no existe
#        raise Http404 #lanza la clase http404
#    return HttpResponse("%s?" % pregunta.asunto)

#El siguiente codigo es un atajo visto anteriomente, es decir lo que hace es que en caso de elegir un numero de pregunta que no exista controla ese error mandando un mensaje.
def pregunta_detalle(self, pregunta_id):
    pregunta = get_object_or_404(Pregunta, pk=pregunta_id)
    return render_to_response("pregunta_detalle.html",{"pregunta":pregunta})
