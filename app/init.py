from app.datos.forms import AltaSocioForm
from app.negocio import SocioNegocio
from flask import Flask, redirect, request, render_template
from app.datos.models import Socio

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


@app.route('/socio/alta', methods=['GET', 'POST'])
def altaSocio():
    form = AltaSocioForm(request.form)
    if request.method == 'POST' and form.validate():
        if socioNegocio.insert_socio(
                Socio(form.dni.data, form.nombre.data, form.apellido.data, form.telefono.data, Socio.ACTIVO)):
            return redirect("socio")
        else:
            message = "Error al insertar el socio"
            return render_template('socio/altaSocio.html', error=message, form=form)
    return render_template('socio/altaSocio.html', form=form)


@app.route('/socio/modificar/<dni>', methods=['GET', 'POST'])
def modificarSocio(dni):
    form = AltaSocioForm(request.form)
    message = ""
    if request.method == 'POST' and form.validate():
        if socioNegocio.update_socio(form.dni.data, form.nombre.data, form.apellido.data, form.telefono.data,
                                     form.activo.data):
            return redirect("socio")
        else:
            message = "Error al modificar el Socio"
    elif request.method == 'GET':
        socio = socioNegocio.get_socios_by_dni(dni)
        if socio:
            form.apellido.data = socio.apellido
            form.nombre.data = socio.nombre
            form.dni.data = socio.dni
            form.telefono.data = socio.telefono
            form.activo.data = socio.activo
        else:
            message = 'No se encontro le Socio con DNI: ' + dni
    return render_template('socio/modificarSocio.html', error=message, form=form)

@app.route('/socio/borrar/<dni>')
def borrarSocio(dni):
    message=""
    if socioNegocio.delete_socio(dni):
        return redirect("socio")
    else:
        message="No se puede eliminar el Socio"
    return render_template('socio/modificarSocio.html', error=message)


@app.route('/socio/')
def socios():
    return render_template('socio/index.html', socios=socioNegocio.get_socios())


@app.route('/altaok')
def altaok():
    return "<h1>Socio ingresado correctamente</h1>"


app.run(debug=True)
