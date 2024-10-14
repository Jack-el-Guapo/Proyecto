from django import forms
from proyectosApp.models import Proyecto

class FormProyecto(forms.modelForm):
    class meta:
        model = Proyecto
        fields = '__all__'