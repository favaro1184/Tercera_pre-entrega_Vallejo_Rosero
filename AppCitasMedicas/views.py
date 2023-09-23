from django.shortcuts import render
from django.http import HttpResponse
from AppCitasMedicas.models import Paciente
from AppCitasMedicas.models import Medico
from AppCitasMedicas.models import Clinica
from AppCitasMedicas.models import Cita
from AppCitasMedicas.forms import PacienteFormulario
from AppCitasMedicas.forms import MedicoFormulario
from AppCitasMedicas.forms import ClinicaFormulario
from AppCitasMedicas.forms import CitaFormulario

############################################################################################################################################
# PAGINA DE INICIO
def inicio(request):
    return render(request, "AppCitasMedicas/inicio.html")


############################################################################################################################################
#CRUD DE PACIENTES  --- CLASICO

#READ ALL  -- Cargar todos los pacientes en la pagina principal de PACIENTES
def ver_pacientes(request):
    pacientes = Paciente.objects.all()
    return render(request, "AppCitasMedicas/ver_pacientes.html", {"res":pacientes})


#CREATE
def crear_pacientes(request):
      if request.method == "POST":
            miFormulario = PacienteFormulario(request.POST) # Aqui me llega la informacion del html
 
            if miFormulario.is_valid():
                  info = miFormulario.cleaned_data
                  paciente = Paciente(id_paciente=info["id_paciente"], nombre=info["nombre"], apellido=info["apellido"], email=info["email"])
                  paciente.save()
                  pacientes_actualizado = Paciente.objects.all()
                  return render(request, "AppCitasMedicas/ver_pacientes.html",{"res":pacientes_actualizado})
      else:
            miFormulario = PacienteFormulario()  #mostramos un formulario vacio
 
      return render(request, "AppCitasMedicas/crear_pacientes.html", {"miFormulario": miFormulario})


#SEARCH - Busqueda individual de profesores
def buscar_pacientes(request):
    return render(request, "AppCitasMedicas/buscar_pacientes.html")

def resultado_pacientes(request):
    if request.GET["id_paciente"]:
        id_paciente = request.GET["id_paciente"]
        paciente_resultado = Paciente.objects.filter(id_paciente__iexact=id_paciente)
        
        return render(request, "AppCitasMedicas/resultado_pacientes.html", {"id_paciente": id_paciente, "res":paciente_resultado})
    
    else: 
        return HttpResponse("No Enviaste datos")
 

############################################################################################################################################
#CRUD DE MEDICOS  --- CLASICO

#READ ALL  -- Cargar todos los medicos en la pagina principal de MEDICOS
def ver_medicos(request):
    medicos = Medico.objects.all()
    return render(request, "AppCitasMedicas/ver_medicos.html", {"res":medicos})


#CREATE
def crear_medicos(request):
      if request.method == "POST":
            miFormulario = MedicoFormulario(request.POST) # Aqui me llega la informacion del html
 
            if miFormulario.is_valid():
                  info = miFormulario.cleaned_data
                  medico = Medico(id_medico=info["id_medico"], nombre=info["nombre"], apellido=info["apellido"], profesion=info["profesion"])
                  medico.save()
                  medicos_actualizado = Medico.objects.all()
                  return render(request, "AppCitasMedicas/ver_medicos.html",{"res":medicos_actualizado})
      else:
            miFormulario = MedicoFormulario()  #mostramos un formulario vacio
 
      return render(request, "AppCitasMedicas/crear_medicos.html", {"miFormulario": miFormulario})


#SEARCH - Busqueda individual de medicos
def buscar_medicos(request):
    return render(request, "AppCitasMedicas/buscar_medicos.html")

def resultado_medicos(request):
    if request.GET["id_medico"]:
        id_medico = request.GET["id_medico"]
        medico_resultado = Medico.objects.filter(id_medico__iexact=id_medico)
        
        return render(request, "AppCitasMedicas/resultado_medicos.html", {"id_paciente": id_medico, "res":medico_resultado})
    
    else: 
        return HttpResponse("No Enviaste datos")


############################################################################################################################################
#CRUD DE CLINICAS  --- CLASICO

#READ ALL  -- Cargar todos las clinicas en la pagina principal de CLINICAS
def ver_clinicas(request):
    clinicas = Clinica.objects.all()
    return render(request, "AppCitasMedicas/ver_clinicas.html", {"res":clinicas})


#CREATE
def crear_clinicas(request):
      if request.method == "POST":
            miFormulario = ClinicaFormulario(request.POST) # Aqui me llega la informacion del html
 
            if miFormulario.is_valid():
                  info = miFormulario.cleaned_data
                  clinica = Clinica(id_clinica=info["id_clinica"], nombre=info["nombre"], direccion=info["direccion"])
                  clinica.save()
                  clinicas_actualizadas = Clinica.objects.all()
                  return render(request, "AppCitasMedicas/ver_clinicas.html",{"res":clinicas_actualizadas})
      else:
            miFormulario = ClinicaFormulario()  #mostramos un formulario vacio
 
      return render(request, "AppCitasMedicas/crear_clinicas.html", {"miFormulario": miFormulario})


#SEARCH - Busqueda individual de clinicas
def buscar_clinicas(request):
    return render(request, "AppCitasMedicas/buscar_clinicas.html")

def resultado_clinicas(request):
    if request.GET["id_clinica"]:
        id_clinica = request.GET["id_clinica"]
        clinica_resultado = Clinica.objects.filter(id_clinica__iexact=id_clinica)
        
        return render(request, "AppCitasMedicas/resultado_clinicas.html", {"id_clinica": id_clinica, "res":clinica_resultado})
    
    else: 
        return HttpResponse("No Enviaste datos")

############################################################################################################################################
#CRUD DE CITAS  --- CLASICO

#READ ALL  -- Cargar todos las citas en la pagina principal de CITAS
def ver_citas(request):
    citas = Cita.objects.all()
    return render(request, "AppCitasMedicas/ver_citas.html", {"res":citas})

#CREATE
def crear_citas(request):
      if request.method == "POST":
            miFormulario = CitaFormulario(request.POST) # Aqui me llega la informacion del html
 
            if miFormulario.is_valid():
                  info = miFormulario.cleaned_data
                  cita = Cita(id_cita=info["id_cita"], id_paciente=info["id_paciente"], id_medico=info["id_medico"], id_clinica=info["id_clinica"], fecha_de_cita=info["fecha_de_cita"])
                  cita.save()
                  citas_actualizadas = Clinica.objects.all()
                  return render(request, "AppCitasMedicas/ver_citas.html",{"res":citas_actualizadas})
      else:
            miFormulario = CitaFormulario()  #mostramos un formulario vacio
 
      return render(request, "AppCitasMedicas/crear_citas.html", {"miFormulario": miFormulario})


#SEARCH - Busqueda individual de clinicas
def buscar_citas(request):
    return render(request, "AppCitasMedicas/buscar_citas.html")

def resultado_citas(request):
    if request.GET["id_cita"]:
        id_cita = request.GET["id_cita"]
        cita_resultado = Cita.objects.filter(id_cita__iexact=id_cita)
        
        return render(request, "AppCitasMedicas/resultado_citas.html", {"id_clinica": id_cita, "res":cita_resultado})
    
    else: 
        return HttpResponse("No Enviaste datos")