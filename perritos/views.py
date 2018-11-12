from django.shortcuts import render
from .models import Contacto
from .models import Nuevo
from perritos.forms import UserForm,UserProfileInfoForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import UserProfileInfo 
from django.views.decorators.csrf import csrf_exempt

def index(request):
    return render(request,'perritos/index.html')

def contacto(request):
    if request.method == 'POST':
        email_m = request.POST.get('txtcorreo')
        rut_m = request.POST.get('txtrut')
        nombre_m = request.POST.get('txtnombre')
        fecha_nac_m = request.POST.get('txtfecha')
        telefono_m = request.POST.get('txttelefono')
        region_m = request.POST.get('cmbregion')
        ciudad_m = request.POST.get('cmbciudad')
        tipo_vivienda_m = request.POST.get('cmbvivienda')
        
        c = Contacto(email=email_m,rut=rut_m,nombre=nombre_m,fecha_nac=fecha_nac_m,telefono=telefono_m,region=region_m,ciudad=ciudad_m,tipo_vivienda=tipo_vivienda_m)
        c.save()
        return render(request,'perritos/answercontacto.html')
    else:
        return render(request,'perritos/Contactanos.html')

def nuevo(request):
    if request.method =='POST':
        rut_dueno_n = request.POST.get('rut_new')
        nom_new_n = request.POST.get('nom_new')
        raza_n = request.POST.get('raza_new')
        descripcion_n = request.POST.get('desc_new')
        foto_n = request.FILES.get('foto_new')
        estado_n = request.POST.get('cmdestado')
        m = Nuevo(rut_dueno=rut_dueno_n,nom=nom_new_n,raza=raza_n,descripcion=descripcion_n,foto=foto_n,estado=estado_n)
        m.save()
        return render(request,'perritos/answernuevo.html')
    else:
        return render(request,'perritos/nuevo.html')

def quienes(request):
    return render(request,'perritos/quienes.html')

def adoptado(request):
    return render(request,'perritos/adoptado.html')

def mostrar2(request):
        nuevito = Nuevo.objects.all()
        contexto = {'nuevo2':nuevito}
        return render(request, 'perritos/mostrar2.html',contexto)

def mostrarcontacto(request):
    conti = Contacto.objects.all()
    contexto2 = {'conta': conti}
    return render(request,'perritos/mostrarcontacto.html',contexto2)


@login_required
def special(request):
    return HttpResponse("Has iniciado sesión correctamente")

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('register'))

def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            if 'foto_perfil' in request.FILES:
                print('found it')
                profile.foto_perfil = request.FILES['foto_perfil']
            profile.save()
            registered = True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
    return render(request,'perritos/registro.html',
                          {'user_form':user_form,
                           'profile_form':profile_form,
                           'registered':registered})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Tu cuenta está inactiva")
        else:
            print("Alguien intentó iniciar sesión y falló")
            print("Usó el usuario: {} y contraseña: {}".format(username,password))
            return HttpResponse("Datos de ingreso incorrectos!")
    else:
        return render(request, 'perritos/login.html', {})


# Create your views here.
