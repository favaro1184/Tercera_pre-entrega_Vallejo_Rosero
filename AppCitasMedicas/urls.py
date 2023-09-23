from django.urls import path
from AppCitasMedicas.views import *

urlpatterns = [
    path('inicio/', inicio, name="Inicio"),
    
    #urls de lectura
    path('pacientes/', ver_pacientes, name="VerPacientes"),
    path('medicos/', ver_medicos, name="VerMedicos"),
    path('clinicas/', ver_clinicas, name="VerClinicas"),
    path('citas/', ver_citas, name="VerCitas"),
    
    #urls de creacion
    path('crearPaciente/', crear_pacientes, name="CrearPacientes"),
    path('crearMedico/', crear_medicos, name="CrearMedicos"),
    path('crearClinica/', crear_clinicas, name="CrearClinicas"),
    path('crearCita/', crear_citas, name="CrearCitas"),
    
    #urls de busqueda
    path('buscarPacientes/', buscar_pacientes, name="BuscarPacientes"),
    path('resultadoPaciente/', resultado_pacientes, name="ResultadoPaciente"),
    path('buscarMedico/', buscar_medicos, name="BuscarMedicos"),
    path('resultadoMedico/', resultado_medicos, name="ResultadoMedico"),
    path('buscarClinica/', buscar_clinicas, name="BuscarClinicas"),
    path('resultadoClinica/', resultado_clinicas, name="ResultadoClinica"),
    path('buscarCita/', buscar_citas, name="BuscarCitas"),
    path('resultadoCita/', resultado_citas, name="ResultadoCita"),

]