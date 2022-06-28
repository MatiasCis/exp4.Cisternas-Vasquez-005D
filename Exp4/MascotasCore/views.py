from django.shortcuts import redirect, render
from django.views.decorators import csrf
from .models import Producto, Cliente
from .forms import ProductoForm, ClienteForm
# Create your views here.

def index(request):
    
    return render(request, 'index.html')

def somos(request):
    return render(request, 'somos.html')

def galeria(request):
    return render(request, 'galeria.html')

def FormReg(request):
    return render(request, 'FormReg.html')

def FormCont(request):
    return render(request, 'FormCont.html')

def Api(request):
    return render(request, 'Api.html')

def MostrarProducto(request):
    productos= Producto.objects.all()
    datos = {
        'productos': productos
    }
    return render(request,'mostrarProducto.html',datos)

def formProducto(request):
    datos = {
        'form':ProductoForm()
    }
    if request.method== 'POST':
        formulario = ProductoForm(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = "Guardados correctamente"
    return render(request, 'formProducto.html',datos)  

def form_mod_producto(request, id):
    producto = Producto.objects.get(idProducto=id)
    datos = {
        'form': ProductoForm(instance = producto)
    }
    if request.method=='POST':
        formulario = ProductoForm(data=request.POST, files=request.FILES, instance = producto)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = "Modificados correctamente"
    
    
        
    return render(request, 'form_mod_producto.html', datos)


def form_del_producto(request, id):
    producto = Producto.objects.get(idProducto=id)
    producto.delete()
    return redirect("MostrarProducto")




def MostrarCliente(request):
    clientes= Cliente.objects.all()
    datos = {
        'clientes': clientes
    }
    return render(request,'mostrarCliente.html',datos)

def formCliente(request):
    datos = {
        'form':ClienteForm()
    }
    if request.method== 'POST':
        formulario = ClienteForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = "Guardados correctamente"
    return render(request, 'formCliente.html',datos)  

def form_mod_cliente(request, id):
    cliente = Cliente.objects.get(rut=id)
    datos = {
        'form': ClienteForm(instance = cliente)
    }
    if request.method=='POST':
        formulario = ClienteForm(data=request.POST, instance = cliente)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = "Modificados correctamente"
        
    return render(request, 'form_mod_cliente.html', datos)

def form_del_cliente(request, id):
    cliente = Cliente.objects.get(rut=id)
    cliente.delete()
    return redirect("MostrarCliente")