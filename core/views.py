from django.shortcuts import render,redirect
from .models import Pelicula
from .forms import PeliculaForm,CustomUserForm
from django.contrib.auth.decorators import login_required,permission_required
from django.contrib.auth import login, authenticate

# Create your views here.

def home(request):
    data = {
        'peliculas':Pelicula.objects.all()
    }

    return render(request,'core/home.html',data)

def galeria(request):

    return render(request,'core/galeria.html')

def listado_peliculas(request):
    peliculas = Pelicula.objects.all()
    data = {
        'peliculas':peliculas
    }

    return render(request,'core/listado_peliculas.html', data)

@permission_required('core.add_pelicula')
def nueva_pelicula(request):
    #ejecuta un insert
    data = {
        'form':PeliculaForm()
    }

    if request.method == 'POST':
        formulario = PeliculaForm(request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = 'Guardado correctamente.'
        data['form'] = formulario

    return render(request,'core/nueva_pelicula.html', data)


def modificar_pelicula(request, id):
    #ejecuta un update
    pelicula = Pelicula.objects.get(id=id) #busca la pelicula
    data = {
        'form':PeliculaForm(instance=pelicula)  #llena el formulario
    }

    if request.method == 'POST':
        formulario = PeliculaForm(data=request.POST, instance=pelicula, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = 'Modificado correctamente.'
        data['form'] = PeliculaForm(instance=Pelicula.objects.get(id=id))

    return render(request,'core/modificar_pelicula.html', data)

def eliminar_pelicula(request, id):
    pelicula = Pelicula.objects.get(id=id) #busca la pelicula
    pelicula.delete()

    return redirect(to='listado_peliculas')

def registro_usuario(request):
    data = {
        'form':CustomUserForm()
    }

    if request.method == 'POST':
        formulario = CustomUserForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            #Autenticar al usuario y redirigirlo al inicio
            username = formulario.cleaned_data['username']
            password = formulario.cleaned_data['password1']
            user = authenticate(username=username,password=password)
            login(request,user)
            return redirect(to='inicio')

        
    return render(request, 'registration/registrar.html',data)
        