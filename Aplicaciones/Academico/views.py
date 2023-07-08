from django.shortcuts import render, redirect
from .models import Curso
from django.contrib import messages

# Create your views here.


def page1(request):
    return render(request, "page1.html", {'navbar': 'page1'})

def page2(request):
    return render(request, "page2.html", {'navbar': 'page2'})

def page3(request):
    return render(request, "page3.html", {'navbar': 'page3'})



def home(request):
    cursosListados = Curso.objects.all()
    messages.success(request, 'Mostrando estaciones')
    return render(request, "gestionCursos.html", {"cursos": cursosListados})

def registrarCurso(request):
    codigo = request.POST['txtCodigo']
    nombre = request.POST['txtNombre']
    creditos = request.POST['numCreditos']

    curso = Curso.objects.create(
        codigo=codigo, nombre=nombre, creditos=creditos)
    messages.success(request, 'Estacion registrada')
    return redirect('/')


def eliminarCurso(request, codigo):
    curso = Curso.objects.get(codigo=codigo)
    curso.delete()

    messages.success(request, 'Estacion eliminada!')

    return redirect('/')


def editarCurso(request):
    codigo = request.POST['txtCodigo']
    nombre = request.POST['txtNombre']
    creditos = request.POST['numCreditos']

    curso = Curso.objects.get(codigo=codigo)
    curso.nombre = nombre
    curso.creditos = creditos
    curso.save()

    messages.success(request, '¡Curso actualizado!')

    return redirect('/')


def edicionCurso(request, codigo):
    curso = Curso.objects.get(codigo=codigo)
    return render(request, "edicionCurso.html", {"curso": curso})
