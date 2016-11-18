from app.negocio import SocioNegocio
from flask import Flask, redirect,request,render_template
from app.datos.models import Socio
from wtforms import Form, StringField, IntegerField, validators, RadioField, FloatField

app = Flask(__name__)

# Configurations
app.config.from_object('config')

socioNegocio = SocioNegocio.SocioNegocio()

@app.route('/')
def hello_world():
    socio = socioNegocio.get_socios()
    return socio[0].nombre

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

@app.route('/getSocioDni=<dni>')
def get_socio_by_dni(dni):
    socio = socioNegocio.get_socios_by_dni(dni)
    return socio.nombre + " " + socio.apellido

# Se crea la clase que luego se renderiza como un formulario con los campos y validaciones especificadas
class AltaSocioForm(Form):
    dni = IntegerField('Dni', [validators.NumberRange(min=1000000, max=100000000, message="Ingrese un DNI correcto")])
    nombre = StringField('Nombre', [validators.Length(min=4, max=30, message="El NOMBRE debe contener por lo menos 4 caracteres y como maximo 30")])
    apellido = StringField('Apellido', [validators.Length(min=4, max=30, message="El APELLIDO debe contener por lo menos 4 caracteres y como maximo 30")])
    telefono = IntegerField('Telefono')
    #edad = IntegerField('Edad', [validators.NumberRange(min=1, max=100,message="Ingrese una edad correcta")])
    #sexo = RadioField('Sexo', choices=[('M', 'Masculino'), ('F', 'Femenino')])

@app.route('/socio/alta', methods=['GET', 'POST'])
def altaSocio():
    form = AltaSocioForm(request.form)
    if request.method == 'POST' and form.validate():
        socio = Socio(form.dni.data, form.nombre.data, form.apellido.data, form.telefono.data, 1)
        try:
            socioNegocio.insert_socio(socio)
            return redirect("altaok")
        except Exception as e:
            message = "Error al insertar el socio"
            return render_template('socio/altaSocio.html', error=message, form=form)

    return render_template('socio/altaSocio.html', form=form)

@app.route('/altaok')
def altaok():
    return "<h1>Socio ingresado correctamente</h1>"

app.run(debug=True)