from wtforms import Form, StringField, IntegerField, validators, RadioField, FloatField


# Se crea la clase que luego se renderiza como un formulario con los campos y validaciones especificadas
class AltaSocioForm(Form):
    dni = IntegerField('Dni', [validators.NumberRange(min=1000000, max=100000000, message="Ingrese un DNI correcto")])
    nombre = StringField('Nombre', [
        validators.Length(min=4, max=30, message="El NOMBRE debe contener por lo menos 4 caracteres y como maximo 30")])
    apellido = StringField('Apellido', [validators.Length(min=4, max=30,
                                                          message="El APELLIDO debe contener por lo menos 4 caracteres y como maximo 30")])
    telefono = IntegerField('Telefono')
    # edad = IntegerField('Edad', [validators.NumberRange(min=1, max=100,message="Ingrese una edad correcta")])
    # sexo = RadioField('Sexo', choices=[('M', 'Masculino'), ('F', 'Femenino')])
