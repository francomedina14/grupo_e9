from django.shortcuts import render, redirect
from .models import Producto

def listar_productos(request):
    productos = Producto.objects.all()
    return render(request, 'index.html', {"productos":productos})

def crear_producto(request):
    # Recibir los datos o atributos
    nombre = request.POST['nombre']
    precio = request.POST['precio']
    existencias = request.POST['existencias']
    # Instanciar un nuevo objeto
    nuevo_producto = Producto(nombre=nombre, precio=precio, existencias=existencias)
    # Guardar y redirigir
    nuevo_producto.save()
    return redirect('/productos/')

def editar_producto(request, pk):
    producto = Producto.objects.get(pk=pk)
    return render(request, 'edit.html', {'producto':producto})

def actualizar_producto(request, pk):
    producto = Producto.objects.get(pk=pk)
    producto.nombre = request.POST['nombre']
    producto.precio = request.POST['precio']
    producto.existencias = request.POST['existencias']
    producto.save()
    return redirect('/productos/')

def eliminar_producto(request, pk):
    producto = Producto.objects.get(pk=pk)
    producto.delete()
    return redirect('/productos/')
