from django import forms

####################################################
# formularios de creacion de datos
####################################################
class PacienteFormulario(forms.Form):
    id_paciente = forms.IntegerField()
    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    email = forms.EmailField()
    
class MedicoFormulario(forms.Form):
    id_medico = forms.IntegerField()
    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    profesion = forms.CharField(max_length=40)
    
class ClinicaFormulario(forms.Form):
    id_clinica = forms.IntegerField()
    nombre = forms.CharField(max_length=40)
    direccion = forms.CharField(max_length=80)
    
class CitaFormulario(forms.Form):
    id_cita = forms.IntegerField()
    id_paciente = forms.IntegerField()
    id_medico = forms.IntegerField()
    id_clinica = forms.IntegerField()
    fecha_de_cita = forms.DateField()