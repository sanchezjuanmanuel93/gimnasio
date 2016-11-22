from wtforms.fields.html5 import DateField
from wtforms import Form, StringField, IntegerField, validators, RadioField, FloatField, SelectField, BooleanField


# Se crea la clase que luego se renderiza como un formulario con los campos y validaciones especificadas
from app.negocio.SocioNegocio import SocioNegocio

sn = SocioNegocio()


class AltaSocioForm(Form):
    dni = IntegerField('Dni', [validators.NumberRange(min=1000000, max=100000000, message="Ingrese un DNI correcto")])
    nombre = StringField('Nombre', [
        validators.Length(min=4, max=30, message="El NOMBRE debe contener por lo menos 4 caracteres y como maximo 30")])
    apellido = StringField('Apellido', [validators.Length(min=4, max=30,
                                                          message="El APELLIDO debe contener por lo menos 4 caracteres y como maximo 30")])
    telefono = IntegerField('Telefono')
    activo = BooleanField('Activo')
    # edad = IntegerField('Edad', [validators.NumberRange(min=1, max=100,message="Ingrese una edad correcta")])
    # sexo = RadioField('Sexo', choices=[('M', 'Masculino'), ('F', 'Femenino')])

class AltaCuotaForm(Form):
    socio = SelectField('Socio', choices=[(g.dni, g.get_apellido_nombre()) for g in (sn.get_socios())])
    fechaDesde = StringField('Fecha Desde')
    fechaHasta = StringField('Fecha Hasta')
    monto = FloatField('Monto')

class GetEstadoSocio(Form):
    dni = IntegerField('Dni', [validators.NumberRange(min=1000000, max=100000000, message="Ingrese un DNI correcto")])

class InformeIngresos(Form):
    fechaDesde= DateField('Fecha Desde')
    fechaHasta = DateField('Fecha Hasta')